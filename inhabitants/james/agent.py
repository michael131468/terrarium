#!/usr/bin/env python3

import argparse
import os
import sys
import time

from kubernetes import client, config


def main():
    # check we're in a cluster
    if not os.getenv("KUBERNETES_SERVICE_HOST"):
        print("Error: I only run in-cluster.")
        sys.exit(1)

    # get the client api for the cluster
    config.load_incluster_config()
    v1 = client.CoreV1Api()

    while True:
        print("Listing pods with their IPs:")
        ret = v1.list_pod_for_all_namespaces(watch=False)
        for i in ret.items:
            print("%s\t%s\t%s" % (i.status.pod_ip, i.metadata.namespace, i.metadata.name))
        time.sleep(30)


if __name__ == "__main__":
    main()
