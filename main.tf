terraform {
  required_version = ">= 1.0.0"
  backend "gcs" {
    bucket = "YOUR_APP_STATE_BUCKET"
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

  template {
    service_account = var.cloudrun_sa_email
    
    containers {
      # Points directly to the image built & pushed during the GitHub Action step
      image = "${var.registry_url}/my-app:${var.image_tag}"
      
      ports {
        container_port = 8080
      }
    }

    # C. Rout traffic natively through your VPC Architecture
    vpc_access {
      connector = var.vpc_connector_id
      egress    = "ALL_TRAFFIC"
    }
  }

  # B. Secure your deployed container using your customer-managed KMS key
  kms_key = var.kms_key_id
}

# Public Access binding (Optional: remove if you want it strictly private inside the VPC)
resource "google_cloud_run_v2_service_iam_member" "public_access" {
  name     = google_cloud_run_v2_service.app_service.name
  location = google_cloud_run_v2_service.app_service.location
  role     = "roles/run.viewer"
  member   = "allUsers"
}
