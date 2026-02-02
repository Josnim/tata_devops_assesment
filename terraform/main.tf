resource "local_file" "infra_info" {
  filename = "infra_deployment.txt"
  content  = "Desplegando Microservicio con 2 replicas y Load Balancer"
}

# replica_count = 2
# load_balancer_enabled = true