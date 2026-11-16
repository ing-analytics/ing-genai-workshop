
# Add the IAM members for the project as 'roles/Owner' to be able to manage all resources in the project.
# All of the ones in locals.project_members should be added as 'roles/Owner' to the project.
resource "google_project_iam_member" "owners" {
  for_each = toset(var.project_members)

  project = var.project_id
  role    = "roles/owner"
  member  = "principal://iam.googleapis.com/locations/global/workforcePools/sandbox-p/subject/${each.key}"
}
