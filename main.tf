terraform {
  required_version = ">= 1.0.0"
  backend "gcs" {
    bucket = "hackathondb2026-cloudrun-app-tfstate-bucket"
    prefix = "app/state"
  }
  required_providers {
    google = {
      source  = "hashicorp/google"
      version = "~> 6.0"
    }
  }
}

provider "google" {
  project = var.project_id
  region  = var.region
}

# --- D & G. CLOUD RUN SERVICE ---
resource "google_cloud_run_v2_service" "app_service" {
  name     = "cloudrun-app-server"
  location = var.region
  ingress  = "INGRESS_TRAFFIC_ALL"
  
  # FIXED: Updated argument name for the Google Provider v6.0+ engine
  deletion_protection = false 

  template {
    service_account = var.cloudrun_sa_email
    encryption_key  = var.kms_key_id
    
    containers {
      image = "${var.registry_url}/my-app:${var.image_tag}"
      
      ports {
        container_port = 8080
      }
    }

    vpc_access {
      connector = var.vpc_connector_id
      egress    = "ALL_TRAFFIC"
    }
  }
}

# Public Access binding
resource "google_cloud_run_v2_service_iam_member" "public_access" {
  name     = google_cloud_run_v2_service.app_service.name
  location = google_cloud_run_v2_service.app_service.location
  member   = "allUsers"
  
  # FIXED: Changed from run.viewer to run.invoker to allow HTTP requests to hit the container
  role     = "roles/run.invoker" 
}
