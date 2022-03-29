from diagrams import Cluster, Diagram, Edge

from diagrams.custom import Custom
from diagrams.onprem.compute import Server

from diagrams.onprem.vcs import Github
from diagrams.generic.os import Ubuntu

from diagrams.generic.virtualization import Vmware
from diagrams.onprem.container import Docker

from diagrams.onprem.iac import Ansible
from diagrams.onprem.iac import Terraform

with Diagram(name="DevOps Initial Process", filename="devops_init", show=False):
  actions = Github("GitHub Actions")
  terraform = Custom("Terraform", "../local_resources/terraform.png")
  packer = Custom("Packer", "../local_resources/packer.png")
  pc = Server("Local Workstation")

  with Cluster("Servers"):
    as01 = Vmware("AS01")
    as02 = Vmware("AS02")
    pc >> Edge(color="orange", style="dotted", label="Initial Setup") \
      >> packer >> Edge(color="orange", style="dotted") \
      >> terraform >> Edge(color="orange", style="dotted")
    terraform >> as01
    terraform >> as02

    with Cluster("GitHub Runner"):
      runner = Ubuntu("Runner")
      ansible = Ansible("Ansible")
      terraform >> Edge(color="orange", style="dotted") \
        >> runner
      actions >> runner
      runner >> Edge(color="green") \
        >> packer >> Edge(color="green", label="Subsequent Actions") \
        >> terraform

    with Cluster("Docker"):
      runner >> ansible
      ansible >> [Docker("S03"),
                  Docker("S02"),
                  Docker("S01")]