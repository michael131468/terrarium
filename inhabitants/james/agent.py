#!/usr/bin/env python3

import argparse
import os
import sys
import time

from dataclasses import dataclass

from kubernetes import client, config


@dataclass
class Feelings:
    happiness: int = 0


def act_v1():
    # do nothing
    pass


def feel_v1():
    feelings = Feelings()

    # More pods, more happiness (up to 100 pods)
    try:
        ret = v1.list_pod_for_all_namespaces(watch=False)
        no_of_pods = len(ret.items)
        feelings.happiness = max(no_of_pods, 100) // 100
    except:
        pass

    return feelings


def main():
    # check we're in a cluster
    if not os.getenv("KUBERNETES_SERVICE_HOST"):
        print("Error: I only run in-cluster.")
        sys.exit(1)

    # get the client api for the cluster
    config.load_incluster_config()
    v1 = client.CoreV1Api()

    while True:
        time.sleep(30)
        feelings = feel_v1(v1)
        print(f"{feelings=}")
        act_v1(feelings)


if __name__ == "__main__":
    main()
