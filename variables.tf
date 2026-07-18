variable "project_id"        { type = string }
variable "region"            { type = string; default = "us-central1" }
variable "vpc_connector_id"  { type = string }
variable "kms_key_id"        { type = string }
variable "cloudrun_sa_email" { type = string }
variable "registry_url"      { type = string }
variable "image_tag"         { type = string; default = "latest" }
