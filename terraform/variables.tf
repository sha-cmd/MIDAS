variable "project_id" {
  description = "ID project GCP"
  default     = "dbtk8s"
  type        = string
}

variable "region" {
  description = "La région GCP"
  default     = "europe-west1"
  type        = string
}

variable "node_count" {
  description = "Nombre de nœuds dans le cluster"
  default     = 2
  type        = number
}
