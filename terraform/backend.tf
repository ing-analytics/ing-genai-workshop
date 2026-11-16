terraform {

  required_providers {
    google = {
      source  = "hashicorp/google"
      version = ">= 6.13"
    }
  }

  required_version = ">= 1.5.0"
}

provider "google" {
  project = var.project_id
  region  = "europe-west4"
}
