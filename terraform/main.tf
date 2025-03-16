provider "google" {
  project = var.project_id
  region  = var.region
  credentials = file("~/git/keys/dbtk8s.json")
}

resource "google_container_cluster" "primary" {
  name     = "dbt-k8s-cluster"
  location = var.region

  remove_default_node_pool = true
  initial_node_count       = 1
  deletion_protection = false
}

resource "google_container_node_pool" "primary_nodes" {
  name       = "dbt-node-pool"
  location   = var.region
  cluster    = google_container_cluster.primary.name
  node_count = var.node_count



  node_config {
    preemptible  = true
    machine_type = "n4-standard-2"
    oauth_scopes = [
      "https://www.googleapis.com/auth/cloud-platform"
    ]
    disk_size_gb = 100
  }



}
