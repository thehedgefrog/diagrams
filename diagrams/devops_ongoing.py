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
  # portainer = Custom ("Portainer", "./local_resources/portainer.png")
  # terraform = Custom("Terraform", "./local_resources/terraform.png")
  # packer = Custom("Packer", "./local_resources/packer.png")
  # ansible = Ansible("Ansible")
  runner = Ubuntu("Runner")

  # with Cluster("Servers"):
  #   as01 = Vmware("AS01")
  #   as02 = Vmware("AS02")
  #   ingress >> packer >> terraform
  #   terraform >> as01
  #   terraform >> as02

  #   with Cluster("GitHub Runner"):
  #
  #     terraform >> runner
  #     ingress >> runner

  with Cluster("Docker"):
    # runner >> ansible
    portainer = Custom ("Portainer", "../local_resources/portainer.png")
    ingress >> runner >> Edge(label="webhook") \
      >> portainer >> [Docker("S01"),
                      Docker("S02"),
                      Docker("S03")]