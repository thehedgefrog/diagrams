from diagrams import Cluster, Diagram, Edge

from diagrams.custom import Custom

from diagrams.onprem.vcs import Github
from diagrams.generic.os import Ubuntu

from diagrams.generic.virtualization import Vmware
from diagrams.onprem.container import Docker

from diagrams.onprem.iac import Ansible
from diagrams.onprem.iac import Terraform

with Diagram(name="DevOps Ongoing Process", filename="devops_ongoing", show=False):
  ingress = Github("GitHub Actions")
  runner = Ubuntu("Runner")

  with Cluster("Docker"):
    portainer = Custom("Portainer", "../local_resources/portainer.png")
    ingress >> runner >> Edge(label="webhook") \
      >> portainer >> [Docker("S01"),
                      Docker("S02"),
                      Docker("S03")]