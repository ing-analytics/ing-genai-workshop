# Enable Artifact Registry API in the GCP project
resource "google_project_service" "artifact_registry" {
  project = var.project_id
  service = "artifactregistry.googleapis.com"
}

# Enable Vertex AI API in the GCP project
resource "google_project_service" "vertex_ai" {
  project = var.project_id
  service = "aiplatform.googleapis.com"
}


# Enable Cloud Run API in the GCP project
resource "google_project_service" "cloud_run" {
  project = var.project_id
  service = "run.googleapis.com"
}

