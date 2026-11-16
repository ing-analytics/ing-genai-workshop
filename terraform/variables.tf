variable "project_id" {
  description = "The ID of the GCP project"
  type        = string
}

variable "project_members" {
  description = "The members of the GCP project"
  type        = list(string)
}

variable "region" {
  description = "The region of the GCP project"
  type        = string
  default     = "europe-west4"
}
