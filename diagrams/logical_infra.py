from diagrams import Cluster, Diagram, Edge

from diagrams.onprem.network import Internet
from diagrams.saas.cdn import Cloudflare
from diagrams.onprem.network import Pfsense
from diagrams.onprem.network import Traefik
from diagrams.onprem.certificates import LetsEncrypt

from diagrams.onprem.database import Mariadb
from diagrams.generic.os import Windows

from diagrams.outscale.security import IdentityAndAccessManagement
from diagrams.aws.network import PublicSubnet
from diagrams.aws.network import PrivateSubnet

with Diagram(name="Logical Infrastructure", show=False):
  ingress = Internet("WAN")
  middleware = Cloudflare("Cloudflare")
  ingress >> middleware

  with Cluster("On-Prem"):
    firewall = Pfsense("pfSense")
    middleware >> firewall

    with Cluster("Docker"):
      traefik = Traefik("Traefik")
      authelia = IdentityAndAccessManagement("Authelia")
      firewall >> traefik >> authelia
      authelia >> PrivateSubnet("Private Containers")
      traefik >> PublicSubnet("Public Containers")

    with Cluster("RS01"):
      ldap = Windows("Server2019 LDAP")
      database = Mariadb("MariaDB")
      ldap - database
      ldap >> authelia
      database >> authelia

    authelia >> PrivateSubnet("Private Services")
    traefik >> PublicSubnet("Public Services")
  LetsEncrypt("Let's Encrypt") >> traefik