resource "google_storage_bucket" "app_data" {
  # Create a bucket for application data
  name          = "${var.project_id}-app-data"
  location      = "EU"
  force_destroy = false

  uniform_bucket_level_access = true

  versioning {
    enabled = true
  }

  public_access_prevention = "enforced"
}

resource "google_storage_bucket_iam_member" "app_data_admins" {
  for_each = toset(var.project_members)


  bucket = google_storage_bucket.app_data.name
  role   = "roles/storage.objectAdmin"
  member = "principal://iam.googleapis.com/locations/global/workforcePools/sandbox-p/subject/${each.key}"
}
