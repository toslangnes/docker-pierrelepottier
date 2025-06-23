## Index

- [Part I : Init](#part-i--init)
- [I. Un premier conteneur en vif](#i-un-premier-conteneur-en-vif)
    - [1. Simple run](#1-simple-run)
    - [2. Volumes](#2-volumes)
    - [3. Variable d'environnement](#3-variable-denvironnement)
- [Part II : Images](#part-ii--images)
- [I. Images publiques](#i-images-publiques)
- [II. Construire une image](#ii-construire-une-image)
    - [A. Build la meow-api](#a-build-la-meow-api)
    - [B. Packagez vous-même une app](#b-packagez-vous-même-une-app)
    - [C. Ecrire votre propre Dockerfile](#c-ecrire-votre-propre-dockerfile)
- [Part III. Compose](#part-iii-compose)
- [I. Getting started](#i-getting-started)
    - [1. Run it](#1-run-it)
    - [2. What about networking](#2-what-about-networking)
- [II. A working meow-api](#ii-a-working-meow-api)
    - [6. Rendu attendu](#6-rendu-attendu)

# Part I : Init

# I. Un premier conteneur en vif

## 1. Simple run

**Lancer un conteneur [`meow_api`](https://hub.docker.com/r/it4lik/meow-api)**

- avec la commande suivante :

```bash
docker run -p 8000:8000 it4lik/meow_api
```

> Ça nous donne ça :

```bash
[09:46:02] pierrelepottier :: Pierres-MacBook-Pro  ➜  ~ » docker run -d -p 8000:8000 it4lik/meow-api:arm
Unable to find image 'it4lik/meow-api:arm' locally
arm: Pulling from it4lik/meow-api
8fbf1dd6492c: Pull complete 
c5e137b9ec17: Pull complete 
14f5719d6358: Pull complete 
78f00d2fce16: Pull complete 
c9871df95570: Pull complete 
c9e098cc9ddd: Pull complete 
ee3677d6f711: Pull complete 
bf8a8047f2c7: Pull complete 
11ceb31c6e90: Pull complete 
7a87bb464191: Pull complete 
4e84d5677718: Pull complete 
Digest: sha256:83ea4c39325a8779baae736be9c18f5a6e26bbe5216c8955aec58c65be7691a9
Status: Downloaded newer image for it4lik/meow-api:arm
6ca1ec3b83026e1b2856c551e22086a1ef18f997d8b2fcf7fc93d9e34ba4c43e
[10:00:20] pierrelepottier :: Pierres-MacBook-Pro  ➜  ~ » 
```

**Visitons**

- vérifier que le conteneur est actif avec une commande qui liste les conteneurs en cours de fonctionnement :

```bash
[10:00:20] pierrelepottier :: Pierres-MacBook-Pro  ➜  ~ » docker ps
CONTAINER ID   IMAGE                 COMMAND           CREATED          STATUS          PORTS                    NAMES
6ca1ec3b8302   it4lik/meow-api:arm   "python app.py"   57 seconds ago   Up 56 seconds   0.0.0.0:8000->8000/tcp   crazy_montalcini
[10:01:16] pierrelepottier :: Pierres-MacBook-Pro  ➜  ~ » 
```

- afficher les logs du conteneur :

> Avec le -f ( --follow), pur stream les logs en continu$

```bash
[10:01:16] pierrelepottier :: Pierres-MacBook-Pro  ➜  ~ » docker logs -f 6ca1ec3b8302    
 * Serving Flask app 'app'
 * Debug mode: on
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on all addresses (0.0.0.0)
 * Running on http://127.0.0.1:8000
 * Running on http://172.17.0.2:8000
Press CTRL+C to quit
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 135-175-261
```

- afficher toutes les informations relatives au conteneur avec une commande `docker inspect` :

```bash
[10:02:29] pierrelepottier :: Pierres-MacBook-Pro  ➜  ~ » docker inspect 6ca1ec3b8302
[
    {
        "Id": "6ca1ec3b83026e1b2856c551e22086a1ef18f997d8b2fcf7fc93d9e34ba4c43e",
        "Created": "2025-06-23T08:00:19.868413043Z",
        "Path": "python",
        "Args": [
            "app.py"
        ],
        "State": {
            "Status": "running",
            "Running": true,
            "Paused": false,
            "Restarting": false,
            "OOMKilled": false,
            "Dead": false,
            "Pid": 666,
            "ExitCode": 0,
            "Error": "",
            "StartedAt": "2025-06-23T08:00:20.219909877Z",
            "FinishedAt": "0001-01-01T00:00:00Z"
        },
        "Image": "sha256:1a14ae666dbae461134e1fc0c4f5552e25e2e9731dab839917059500f0705ba1",
        "ResolvConfPath": "/var/lib/docker/containers/6ca1ec3b83026e1b2856c551e22086a1ef18f997d8b2fcf7fc93d9e34ba4c43e/resolv.conf",
        "HostnamePath": "/var/lib/docker/containers/6ca1ec3b83026e1b2856c551e22086a1ef18f997d8b2fcf7fc93d9e34ba4c43e/hostname",
        "HostsPath": "/var/lib/docker/containers/6ca1ec3b83026e1b2856c551e22086a1ef18f997d8b2fcf7fc93d9e34ba4c43e/hosts",
        "LogPath": "/var/lib/docker/containers/6ca1ec3b83026e1b2856c551e22086a1ef18f997d8b2fcf7fc93d9e34ba4c43e/6ca1ec3b83026e1b2856c551e22086a1ef18f997d8b2fcf7fc93d9e34ba4c43e-json.log",
        "Name": "/crazy_montalcini",
        "RestartCount": 0,
        "Driver": "overlay2",
        "Platform": "linux",
        "MountLabel": "",
        "ProcessLabel": "",
        "AppArmorProfile": "",
        "ExecIDs": null,
        "HostConfig": {
            "Binds": null,
            "ContainerIDFile": "",
            "LogConfig": {
                "Type": "json-file",
                "Config": {}
            },
            "NetworkMode": "bridge",
            "PortBindings": {
                "8000/tcp": [
                    {
                        "HostIp": "",
                        "HostPort": "8000"
                    }
                ]
            },
            "RestartPolicy": {
                "Name": "no",
                "MaximumRetryCount": 0
            },
            "AutoRemove": false,
            "VolumeDriver": "",
            "VolumesFrom": null,
            "ConsoleSize": [
                55,
                90
            ],
            "CapAdd": null,
            "CapDrop": null,
            "CgroupnsMode": "private",
            "Dns": [],
            "DnsOptions": [],
            "DnsSearch": [],
            "ExtraHosts": null,
            "GroupAdd": null,
            "IpcMode": "private",
            "Cgroup": "",
            "Links": null,
            "OomScoreAdj": 0,
            "PidMode": "",
            "Privileged": false,
            "PublishAllPorts": false,
            "ReadonlyRootfs": false,
            "SecurityOpt": null,
            "UTSMode": "",
            "UsernsMode": "",
            "ShmSize": 67108864,
            "Runtime": "runc",
            "Isolation": "",
            "CpuShares": 0,
            "Memory": 0,
            "NanoCpus": 0,
            "CgroupParent": "",
            "BlkioWeight": 0,
            "BlkioWeightDevice": [],
            "BlkioDeviceReadBps": [],
            "BlkioDeviceWriteBps": [],
            "BlkioDeviceReadIOps": [],
            "BlkioDeviceWriteIOps": [],
            "CpuPeriod": 0,
            "CpuQuota": 0,
            "CpuRealtimePeriod": 0,
            "CpuRealtimeRuntime": 0,
            "CpusetCpus": "",
            "CpusetMems": "",
            "Devices": [],
            "DeviceCgroupRules": null,
            "DeviceRequests": null,
            "MemoryReservation": 0,
            "MemorySwap": 0,
            "MemorySwappiness": null,
            "OomKillDisable": null,
            "PidsLimit": null,
            "Ulimits": [],
            "CpuCount": 0,
            "CpuPercent": 0,
            "IOMaximumIOps": 0,
            "IOMaximumBandwidth": 0,
            "MaskedPaths": [
                "/proc/asound",
                "/proc/acpi",
                "/proc/interrupts",
                "/proc/kcore",
                "/proc/keys",
                "/proc/latency_stats",
                "/proc/timer_list",
                "/proc/timer_stats",
                "/proc/sched_debug",
                "/proc/scsi",
                "/sys/firmware",
                "/sys/devices/virtual/powercap"
            ],
            "ReadonlyPaths": [
                "/proc/bus",
                "/proc/fs",
                "/proc/irq",
                "/proc/sys",
                "/proc/sysrq-trigger"
            ]
        },
        "GraphDriver": {
            "Data": {
                "ID": "6ca1ec3b83026e1b2856c551e22086a1ef18f997d8b2fcf7fc93d9e34ba4c43e",
                "LowerDir": "/var/lib/docker/overlay2/ca099b679a0db03b3d19c62aa9e1e26ce868bb128710992bd07c3eb168f7d451-init/diff:/var/lib/docker/overlay2/92bf79ec4f5d1fb01ff6c5561c89f8bffc63260c05ec8262dcc7f60ece469f6d/diff:/var/lib/docker/overlay2/424301f0bceffab6e23314341aaf2f5a68cdc98719c9335f67fae76db55e069f/diff:/var/lib/docker/overlay2/39289bac06fcd74e0135873146a13e827bf4983e8b862c4c0b229163e70ffa57/diff:/var/lib/docker/overlay2/01c219128f8b749fc84666102ce419908fa05996178bd9750a80eebb067157aa/diff:/var/lib/docker/overlay2/3254380e0373350b407f0604f61e72a20c0631f08ed86480442acbcca18d8d48/diff:/var/lib/docker/overlay2/f2ace2522c07ba5b9557df9aaa87218f575cce6399949767262fe8cb832d199c/diff:/var/lib/docker/overlay2/ea12c4e15b474e7694f3a4c7c3e897c8e82a37baa5cc572a3a2dde8e4c6a057e/diff:/var/lib/docker/overlay2/e423d3d736c110df8ee6563e7b2059e6e9a492b3687ff910a46e0752a72924ed/diff:/var/lib/docker/overlay2/43757d57ff967b8d4f83c5160bfd6f5440b04ed827b2d4220c10f200b3aa1e8a/diff:/var/lib/docker/overlay2/f7535a4c00c563d529da2a80590b245b837d7174061171459a872584a1d6d820/diff:/var/lib/docker/overlay2/e5f2e075a0c2ed9f8d04c7df44f17434f2fda11891df41fb1bc092faf89db1b9/diff",
                "MergedDir": "/var/lib/docker/overlay2/ca099b679a0db03b3d19c62aa9e1e26ce868bb128710992bd07c3eb168f7d451/merged",
                "UpperDir": "/var/lib/docker/overlay2/ca099b679a0db03b3d19c62aa9e1e26ce868bb128710992bd07c3eb168f7d451/diff",
                "WorkDir": "/var/lib/docker/overlay2/ca099b679a0db03b3d19c62aa9e1e26ce868bb128710992bd07c3eb168f7d451/work"
            },
            "Name": "overlay2"
        },
        "Mounts": [],
        "Config": {
            "Hostname": "6ca1ec3b8302",
            "Domainname": "",
            "User": "",
            "AttachStdin": false,
            "AttachStdout": false,
            "AttachStderr": false,
            "ExposedPorts": {
                "8000/tcp": {}
            },
            "Tty": false,
            "OpenStdin": false,
            "StdinOnce": false,
            "Env": [
                "PATH=/usr/local/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin",
                "GPG_KEY=7169605F62C751356D054A26A821E680E5FA6305",
                "PYTHON_VERSION=3.13.5",
                "PYTHON_SHA256=93e583f243454e6e9e4588ca2c2662206ad961659863277afcdb96801647d640"
            ],
            "Cmd": [
                "python",
                "app.py"
            ],
            "Image": "it4lik/meow-api:arm",
            "Volumes": null,
            "WorkingDir": "/app",
            "Entrypoint": null,
            "OnBuild": null,
            "Labels": {}
        },
        "NetworkSettings": {
            "Bridge": "",
            "SandboxID": "3af223c45a2f04d7c4f37614db065160d05938553a44c06165d15390a051ab63",
            "SandboxKey": "/var/run/docker/netns/3af223c45a2f",
            "Ports": {
                "8000/tcp": [
                    {
                        "HostIp": "0.0.0.0",
                        "HostPort": "8000"
                    }
                ]
            },
            "HairpinMode": false,
            "LinkLocalIPv6Address": "",
            "LinkLocalIPv6PrefixLen": 0,
            "SecondaryIPAddresses": null,
            "SecondaryIPv6Addresses": null,
            "EndpointID": "1722048c5d04943e38a2fdd9c13f80b71791891cc24726933206b54faff32479",
            "Gateway": "172.17.0.1",
            "GlobalIPv6Address": "",
            "GlobalIPv6PrefixLen": 0,
            "IPAddress": "172.17.0.2",
            "IPPrefixLen": 16,
            "IPv6Gateway": "",
            "MacAddress": "66:28:30:5f:ad:8f",
            "Networks": {
                "bridge": {
                    "IPAMConfig": null,
                    "Links": null,
                    "Aliases": null,
                    "MacAddress": "66:28:30:5f:ad:8f",
                    "DriverOpts": null,
                    "GwPriority": 0,
                    "NetworkID": "74cd24bd8cd1a5ba352c830e64cab351f81d0e5e2299fddcb7a5aa9c10c9b89c",
                    "EndpointID": "1722048c5d04943e38a2fdd9c13f80b71791891cc24726933206b54faff32479",
                    "Gateway": "172.17.0.1",
                    "IPAddress": "172.17.0.2",
                    "IPPrefixLen": 16,
                    "IPv6Gateway": "",
                    "GlobalIPv6Address": "",
                    "GlobalIPv6PrefixLen": 0,
                    "DNSNames": null
                }
            }
        }
    }
]
```

---

**Lancer le conteneur en tâche de fond**

```bash
docker run -d -p 8000:8000 it4lik/meow-api:arm
```

```bash
[10:04:35] pierrelepottier :: Pierres-MacBook-Pro  ➜  ~ » docker run -d -p 8000:8000 it4lik/meow-api:arm
ac7d52f17e4404ff501bcbe2067945e8c519ce01afb8c12bb778538a5b9e513e
[10:04:41] pierrelepottier :: Pierres-MacBook-Pro  ➜  ~ »
```

**Consultez les logs du conteneur**

- avec une commande `docker logs`, il faudra préciser l'ID ou le nom du conteneur en argument à la commande :

```bash
[10:04:41] pierrelepottier :: Pierres-MacBook-Pro  ➜  ~ » docker ps
CONTAINER ID   IMAGE                 COMMAND           CREATED          STATUS          PORTS                    NAMES
ac7d52f17e44   it4lik/meow-api:arm   "python app.py"   37 seconds ago   Up 37 seconds   0.0.0.0:8000->8000/tcp   relaxed_hugle
[10:05:18] pierrelepottier :: Pierres-MacBook-Pro  ➜  ~ » docker logs relaxed_hugle
* Serving Flask app 'app'
* Debug mode: on
  WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
* Running on all addresses (0.0.0.0)
* Running on http://127.0.0.1:8000
* Running on http://172.17.0.2:8000
  Press CTRL+C to quit
* Restarting with stat
* Debugger is active!
* Debugger PIN: 563-020-946
  [10:05:31] pierrelepottier :: Pierres-MacBook-Pro  ➜  ~ »
```

## 2. Volumes

**Remplacer le code `app.py`**

```bash
[10:10:53] pierrelepottier :: Pierres-MacBook-Pro  ➜  IntelliJProjects/docker-pierrelepottier/tp1 ‹main*› » docker run -d --name meow-override -p 8000:8000 -v $(pwd)/app.py:/app/app.py it4lik/meow-api:arm
071062595d2ebd4441af8d93d7adcb7e4c0d5db21f1476dbbb0606693a14a4a1
```

**Prouvez que ça fonctionne avec une requête Web**

```bash
[10:14:28] pierrelepottier :: Pierres-MacBook-Pro  ➜  IntelliJProjects/docker-pierrelepottier/tp1 ‹main*› » curl http://localhost:8000/

            <h1>Wild Kitty Override!</h1>
            <img src="https://media.giphy.com/media/JIX9t2j0ZTN9S/giphy.gif" alt="kitty gif">
```

## 3. Variable d'environnement

**Définir une variable d'environnement au lancement du conteneur**

- ajoutez une option sur le `docker run` pour lancer l'image `it4lik/meow-api` en définissant une variable
  d'environnement
- doit définir la variable d'environnement mentionnée plus haut
- écoutez sur le port `7000` (6000 sur mac)

**Mettez à jour l'option `-p`**

```bash
[10:39:01] pierrelepottier :: Pierres-MacBook-Pro  ➜  ~ » docker run -d --name meow-env -e LISTEN_PORT=6000 -p 6000:6000 it4lik/meow-api:arm
6faf893a805d7247a13af4cd4ab588755889ffe7f8a06d89dd6fd59a895cee88
[10:39:47] pierrelepottier :: Pierres-MacBook-Pro  ➜  ~ » 
```

**Prouvez que ça fonctionne avec une requête Web**

```bash
[10:39:47] pierrelepottier :: Pierres-MacBook-Pro  ➜  ~ » curl http://localhost:6000/
{"message":"Available routes","routes":{"get_user_by_id":"http://localhost:6000/user/1","list_all_users":"http://localhost:6000/users"}}
[10:40:22] pierrelepottier :: Pierres-MacBook-Pro  ➜  ~ » 
```

# Part II : Images

# I. Images publiques

**Récupérez des images**

- avec la commande `docker pull`
- récupérez :
    - l'image `python` officielle en version 3.11 (`python:3.11` pour la dernière version)
    - l'image `mysql` officielle en version 5.7 (8)
    - l'image `wordpress` officielle en dernière version
        - c'est le tag `:latest` pour récupérer la dernière version
        - si aucun tag n'est précisé, `:latest` est automatiquement ajouté
    - l'image `linuxserver/wikijs` en dernière version
        - ce n'est pas une image officielle car elle est hébergée par l'utilisateur `linuxserver` contrairement aux 3
          précédentes
        - on doit donc avoir un moins haut niveau de confiance en cette image
- listez les images que vous avez sur la machine avec une commande `docker`

```bash
[10:41:35] pierrelepottier :: Pierres-MacBook-Pro  ➜  ~ » docker pull python:3.11
3.11: Pulling from library/python
8fbf1dd6492c: Pull complete 
c5e137b9ec17: Pull complete 
14f5719d6358: Pull complete 
78f00d2fce16: Pull complete 
7b9f5f869a6e: Pull complete 
828a2a41375b: Pull complete 
c016ca73232f: Pull complete 
Digest: sha256:ce3b954c9285a7a145cba620bae03db836ab890b6b9e0d05a3ca522ea00dfbc9
Status: Downloaded newer image for python:3.11
docker.io/library/python:3.11

What's next:
    View a summary of image vulnerabilities and recommendations → docker scout quickview python:3.11
[10:48:50] pierrelepottier :: Pierres-MacBook-Pro  ➜  ~ » docker pull mysql:5.7
5.7: Pulling from library/mysql
no matching manifest for linux/arm64/v8 in the manifest list entries
[10:48:54] pierrelepottier :: Pierres-MacBook-Pro  ➜  ~ » docker pull mysql:8.0       1 ↵
8.0: Pulling from library/mysql
1281dea9bbdc: Pull complete 
65a492f1b8dd: Pull complete 
12d652dc2508: Pull complete 
cffd736c905d: Pull complete 
147b5c0a118e: Pull complete 
0984c0aea400: Pull complete 
1a9c3e4b007a: Pull complete 
7dac163d5ad3: Pull complete 
85065940bba5: Pull complete 
5ce44a171d06: Pull complete 
9c7266afaf33: Pull complete 
Digest: sha256:98914997054781e301d675233d76f393168ea67002424c5291072e5593350e1b
Status: Downloaded newer image for mysql:8.0
docker.io/library/mysql:8.0

What's next:
    View a summary of image vulnerabilities and recommendations → docker scout quickview mysql:8.0
[10:49:49] pierrelepottier :: Pierres-MacBook-Pro  ➜  ~ » docker pull wordpress:latest
latest: Pulling from library/wordpress
34ef2a75627f: Pull complete 
3630c4a6bfab: Pull complete 
877a4d3e37c3: Pull complete 
39acdc354785: Pull complete 
3fff45d01fc3: Pull complete 
a25063be4912: Pull complete 
f8dd604a657c: Pull complete 
3328044d89bc: Pull complete 
24fdd0d074fa: Pull complete 
c2a5deda81d7: Pull complete 
b29695fa5193: Pull complete 
afd2e054d8d1: Pull complete 
a543208f4efc: Pull complete 
4f4fb700ef54: Pull complete 
68dcd2860c81: Pull complete 
f79b6cf338f4: Pull complete 
5ba2a3743b4b: Pull complete 
02c79cd8699c: Pull complete 
e5986a134440: Pull complete 
211625f3b9f3: Pull complete 
0c3f64a2b782: Pull complete 
cbda9f6cd672: Pull complete 
Digest: sha256:1931132b0b93230ee44d9628868e3ffe2076f49ba6569b36d281c0ccaa618ef4
Status: Downloaded newer image for wordpress:latest
docker.io/library/wordpress:latest

What's next:
    View a summary of image vulnerabilities and recommendations → docker scout quickview wordpress:latest
[10:50:05] pierrelepottier :: Pierres-MacBook-Pro  ➜  ~ » docker pull linuxserver/wikijs:latest
latest: Pulling from linuxserver/wikijs
8423e39ae289: Pull complete 
e1cde46db0e1: Pull complete 
bc92fab8947f: Pull complete 
8e2f36998bea: Pull complete 
e7e33b357221: Pull complete 
33fedb35122c: Pull complete 
0c12cf8e3fe6: Pull complete 
1bfc3bc05ba0: Pull complete 
b099656749ad: Pull complete 
Digest: sha256:f997a921b7695fc7528740ad2c36c10b0b9c23b2878a937487367ad98df15591
Status: Downloaded newer image for linuxserver/wikijs:latest
docker.io/linuxserver/wikijs:latest

What's next:
    View a summary of image vulnerabilities and recommendations → docker scout quickview linuxserver/wikijs:latest
```

```bash
[10:50:28] pierrelepottier :: Pierres-MacBook-Pro  ➜  ~ » docker images
REPOSITORY           TAG       IMAGE ID       CREATED        SIZE
linuxserver/wikijs   latest    de6588eb7efe   9 days ago     494MB
python               3.11      119ba481a16b   2 weeks ago    1.02GB
wordpress            latest    b4344f7748b7   7 weeks ago    699MB
mysql                8.0       768a378c6148   2 months ago   768MB
[10:51:01] pierrelepottier :: Pierres-MacBook-Pro  ➜  ~ » 
```

**Lancez un conteneur à partir de l'image Python**

- lancez un terminal `bash` ou `sh` à l'intérieur du conteneur
- vérifiez que la commande `python` est installée dans le conteneur, à la bonne version

```bash
[10:53:22] pierrelepottier :: Pierres-MacBook-Pro  ➜  ~ » docker run --rm -it python:3.11 bash
root@e068277e56bf:/# python --version
Python 3.11.13
root@e068277e56bf:/# 
```

# II. Construire une image

## A. Build la meow-api

**Récupérer le code et le `Dockerfile` sur votre machine**

- vrai tech le fait avec une commande et la met dans le compte-rendu
- créer un dossier et déplacer dedans le fichier de code et le `Dockerfile`

```bash
[10:58:30] pierrelepottier :: Pierres-MacBook-Pro  ➜  ~/IntelliJProjects » git clone https://gitlab.com/it4lik/b3e-docker-avance.git
Cloning into 'b3e-docker-avance'...
remote: Enumerating objects: 59, done.
remote: Counting objects: 100% (59/59), done.
remote: Compressing objects: 100% (54/54), done.
remote: Total 59 (delta 18), reused 0 (delta 0), pack-reused 0 (from 0)
Receiving objects: 100% (59/59), 1.56 MiB | 16.02 MiB/s, done.
Resolving deltas: 100% (18/18), done.
[10:58:38] pierrelepottier :: Pierres-MacBook-Pro  ➜  ~/IntelliJProjects » cd b3e-docker-avance/tp/1/app
[10:58:45] pierrelepottier :: Pierres-MacBook-Pro  ➜  tp/1/app ‹main› » ls
app.py           Dockerfile       Dockerfile   requirements.txt
[10:58:49] pierrelepottier :: Pierres-MacBook-Pro  ➜  tp/1/app ‹main› » mv ~/IntelliJProjects/b3e-docker-avance/tp/1/app/{app.py,Dockerfile,requirements.txt} ~/IntelliJProjects/docker-pierrelepottier/tp1/app/                 
[11:01:29] pierrelepottier :: Pierres-MacBook-Pro  ➜  tp/1/app ‹main*› » 
```

**Build une image `meow-api`**

- depuis un terminal, déplacez-vous dans le dossier qui contient le `Dockerfile`
- exécutez la commande :

```bash
# le caractère . fait référence au dossier actuel : le contexte de build
# -t permet de préciser un "tag" : le nom de l'image
docker build . -t meow-api
```

```bash
[11:03:08] pierrelepottier :: Pierres-MacBook-Pro  ➜  docker-pierrelepottier/tp1/app ‹main*› » docker build . -f Dockerfile -t meow-api-arm
[+] Building 8.8s (11/11) FINISHED                                   docker:desktop-linux
 => [internal] load build definition from Dockerfile                             0.0s
 => => transferring dockerfile: 563B                                                 0.0s
 => [internal] load metadata for docker.io/library/python:3                          1.6s
 => [auth] library/python:pull token for registry-1.docker.io                        0.0s
 => [internal] load .dockerignore                                                    0.0s
 => => transferring context: 2B                                                      0.0s
 => [1/5] FROM docker.io/library/python:3@sha256:5f69d22a88dd4cc4ee1576def19aef48c8  2.7s
 => => resolve docker.io/library/python:3@sha256:5f69d22a88dd4cc4ee1576def19aef48c8  0.0s
 => => sha256:2af41c79cd3c19ebc1465b853b99b5b7431f36e1f85b983b51c7f 2.33kB / 2.33kB  0.0s
 => => sha256:e5664608d2f363604c87c075fc194539e6659e5343751355f978c 6.34kB / 6.34kB  0.0s
 => => sha256:c9871df9557058eda55bc5eb98f33dbe7b130e01e56fe9a7fd162 6.24MB / 6.24MB  0.8s
 => => sha256:ee3677d6f711bfdd806847cb63cbc2f958e0faac82e8521f2e122aef6 250B / 250B  0.5s
 => => sha256:5f69d22a88dd4cc4ee1576def19aef48c8faa1b566054c4429118 9.72kB / 9.72kB  0.0s
 => => sha256:c9e098cc9dddde85c4f6484aeb92d06eaec7925326ca18df401 26.65MB / 26.65MB  2.1s
 => => extracting sha256:c9871df9557058eda55bc5eb98f33dbe7b130e01e56fe9a7fd162460dd  0.2s
 => => extracting sha256:c9e098cc9dddde85c4f6484aeb92d06eaec7925326ca18df401a19c396  0.5s
 => => extracting sha256:ee3677d6f711bfdd806847cb63cbc2f958e0faac82e8521f2e122aef63  0.0s
 => [internal] load build context                                                    0.0s
 => => transferring context: 1.62kB                                                  0.0s
 => [2/5] WORKDIR /app                                                               0.1s
 => [3/5] COPY ./requirements.txt .                                                  0.0s
 => [4/5] RUN pip install --no-cache-dir -r requirements.txt                         4.2s
 => [5/5] COPY ./app.py .                                                            0.0s 
 => exporting to image                                                               0.2s 
 => => exporting layers                                                              0.2s 
 => => writing image sha256:172a6f81ea74fde78da895c0e859f6b8af47c11a558f1b46420c136  0.0s 
 => => naming to docker.io/library/meow-api-arm                                      0.0s 
                                                                                          
View build details: docker-desktop://dashboard/build/desktop-linux/desktop-linux/9qxdw25ubslhfpvyy5oaznlyx

What's next:
    View a summary of image vulnerabilities and recommendations → docker scout quickview 
[11:03:38] pierrelepottier :: Pierres-MacBook-Pro  ➜  docker-pierrelepottier/tp1/app ‹main*› » 
```

**Afficher la liste des images dispos sur votre machine**

- dans la sortie de la commande, on devrait voir `meow-api` que vous venez de build

```bash
[11:04:42] pierrelepottier :: Pierres-MacBook-Pro  ➜  ~ » docker images
REPOSITORY           TAG       IMAGE ID       CREATED              SIZE
meow-api-arm         latest    172a6f81ea74   About a minute ago   1.13GB
```

**Run cette image**

- faites un `docker run` qui lance l'image nouvellement build

```bash
[11:04:43] pierrelepottier :: Pierres-MacBook-Pro  ➜  ~ » docker run meow-api-arm
* Serving Flask app 'app'
* Debug mode: off
  WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
* Running on all addresses (0.0.0.0)
* Running on http://127.0.0.1:8000
* Running on http://172.17.0.2:8000
  Press CTRL+C to quit
```

## B. Packagez vous-même une app

Voilà un bout de code Python tout naze :

```python
import emoji

print(emoji.emojize("Cet exemple d'application est vraiment naze :thumbs_down:"))
```

**Ecrire un `Dockerfile` pour packager ce code**

- inspirez-vous de la structure de mon [`app/`](./app/) et du [`Dockerfile`](./app/Dockerfile) qu'il contient
- réservez encore un nouveau dossier sur votre machine pour stocker le code et son `Dockerfile`

```bash
FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app.py .

CMD ["python", "app.py"]
```

**Build l'image**

- déplace-toi dans ton répertoire
- `docker build . -t python_app:version_de_ouf`

```bash
[11:11:57] pierrelepottier :: Pierres-MacBook-Pro  ➜  docker-pierrelepottier/tp1/python-app-naze ‹main*› » docker build . -t python_app:version_de_ouf
[+] Building 4.9s (11/11) FINISHED                                   docker:desktop-linux
 => [internal] load build definition from Dockerfile                                 0.0s
 => => transferring dockerfile: 228B                                                 0.0s
 => [internal] load metadata for docker.io/library/python:3.12-slim                  1.5s
 => [auth] library/python:pull token for registry-1.docker.io                        0.0s
 => [internal] load .dockerignore                                                    0.0s
 => => transferring context: 2B                                                      0.0s
 => [1/5] FROM docker.io/library/python:3.12-slim@sha256:e55523f127124e5edc03ba201e  1.6s
 => => resolve docker.io/library/python:3.12-slim@sha256:e55523f127124e5edc03ba201e  0.0s
 => => sha256:0e8765364dfd3a97400f104ab8cec2abe4ad6134aab4762f8559f 5.59kB / 5.59kB  0.0s
 => => sha256:6939e8b629d325c16aec26f961a50f26060da987c2aea1eb86a3e 3.33MB / 3.33MB  0.5s
 => => sha256:168e3ef0fb427aed760a5f876df36877f762b8a3cd10f250dc9 13.59MB / 13.59MB  1.1s
 => => sha256:bfef920e18d403bcc9d4d44db6fd038cd01e033b487f1a9d861fa77b4 249B / 249B  0.6s
 => => sha256:e55523f127124e5edc03ba201e3dbbc85172a2ec40d8651ac7523 9.13kB / 9.13kB  0.0s
 => => sha256:36af0102f0003eb23a19b1e6aa866b9f9ea415cfa5da8b4f3b013 1.75kB / 1.75kB  0.0s
 => => extracting sha256:6939e8b629d325c16aec26f961a50f26060da987c2aea1eb86a3e7e7e8  0.1s
 => => extracting sha256:168e3ef0fb427aed760a5f876df36877f762b8a3cd10f250dc99677956  0.4s
 => => extracting sha256:bfef920e18d403bcc9d4d44db6fd038cd01e033b487f1a9d861fa77b4e  0.0s
 => [internal] load build context                                                    0.0s
 => => transferring context: 252B                                                    0.0s
 => [2/5] WORKDIR /app                                                               0.0s
 => [3/5] COPY requirements.txt .                                                    0.0s
 => [4/5] RUN pip install --no-cache-dir -r requirements.txt                         1.6s
 => [5/5] COPY app.py .                                                              0.0s
 => exporting to image                                                               0.1s
 => => exporting layers                                                              0.0s
 => => writing image sha256:9bd863483a0ccd77a89518d00440ac5dfb706d278926a96f8843b1b  0.0s 
 => => naming to docker.io/library/python_app:version_de_ouf                         0.0s 
                                                                                          
View build details: docker-desktop://dashboard/build/desktop-linux/desktop-linux/k6xgwha6szho5yizxpboyh0aw

What's next:
    View a summary of image vulnerabilities and recommendations → docker scout quickview 
[11:12:05] pierrelepottier :: Pierres-MacBook-Pro  ➜  docker-pierrelepottier/tp1/python-app-naze ‹main*› » 
```

**Proof !**

- une fois le build terminé, constater que l'image est dispo avec une commande `docker`
-

```bash
REPOSITORY           TAG              IMAGE ID       CREATED          SIZE
python_app           version_de_ouf   9bd863483a0c   41 seconds ago   162MB
```

**Lancer l'image**

- lance l'image avec `docker run` :

```bash
docker run python_app:version_de_ouf
```

```bash
[11:12:46] pierrelepottier :: Pierres-MacBook-Pro  ➜  docker-pierrelepottier/tp1/python-app-naze ‹main*› » docker run python_app:version_de_ouf
Cet exemple d'application est vraiment naze 👎
[11:13:14] pierrelepottier :: Pierres-MacBook-Pro  ➜  docker-pierrelepottier/tp1/python-app-naze ‹main*› » 
```

## C. Ecrire votre propre Dockerfile

➜ **Pour cette partie, récupérer un bout de code à vous**

- de préférence un service HTTP, un front web ou une API, peu importe
- t'as bien un truc qui traîne, un exo tout simple d'un autre cours ou quoi
- un truc standalone : qui a pas besoin de db ou quoi

**Ecrire un Dockerfile pour packager votre application**, il contient notamment :

- **`FROM`** : doit partir d'une image officielle
- **`COPY`** : ajoute le code dans l'image
- **`CMD`** : définit la commande à lancer quand le conteneur démarre

```bash
FROM golang:1.21

# Set destination for COPY
WORKDIR /app

# Download Go modules
COPY go.mod go.sum ./
RUN go mod download

# Copy the source code. Note the slash at the end, as explained in
# https://docs.docker.com/reference/dockerfile/#copy
COPY *.go ./

# Build
RUN CGO_ENABLED=0 GOOS=linux go build -o /docker-gs-ping

# Optional:
# To bind to a TCP port, runtime parameters must be supplied to the docker command.
# But we can document in the Dockerfile what ports
# the application is going to listen on by default.
# https://docs.docker.com/reference/dockerfile/#expose
EXPOSE 8080

# Run
CMD ["/docker-gs-ping"]
```

**Publiez votre image sur le Docker Hub**

- faut se créer un compte sur la WebUi du Docker Hub
- faut créer un *repository* depuis la WebUi, une fois connecté
- faut nommer correctement votre image, avec votre user dedans
- et `docker push`
- dans le compte-rendu je veux :
    - toutes les commandes que vous avez tapées
    - l'URL de votre image sur la WebUI du Docker Hub

```bash
[11:47:23] pierrelepottier :: Pierres-MacBook-Pro  ➜  docker-pierrelepottier/tp1/sample_app ‹main*› » docker build --tag pierre .
[+] Building 4.4s (11/11) FINISHED                                   docker:desktop-linux
 => [internal] load build definition from Dockerfile                                 0.0s
 => => transferring dockerfile: 696B                                                 0.0s
 => [internal] load metadata for docker.io/library/golang:1.21                       0.0s
 => [internal] load .dockerignore                                                    0.0s
 => => transferring context: 2B                                                      0.0s
 => [1/6] FROM docker.io/library/golang:1.21                                         0.0s
 => [internal] load build context                                                    0.0s
 => => transferring context: 1.18kB                                                  0.0s
 => [2/6] WORKDIR /app                                                               0.0s
 => [3/6] COPY go.mod go.sum ./                                                      0.0s
 => [4/6] RUN go mod download                                                        0.6s
 => [5/6] COPY *.go ./                                                               0.0s
 => [6/6] RUN CGO_ENABLED=0 GOOS=linux go build -o /docker-gs-ping                   3.5s
 => exporting to image                                                               0.2s
 => => exporting layers                                                              0.2s
 => => writing image sha256:5da615c6ccd28d619566a67653aedf375594d7089439a33da4c7228  0.0s
 => => naming to docker.io/library/pierre                                            0.0s

View build details: docker-desktop://dashboard/build/desktop-linux/desktop-linux/use46h4atzrkqw5b886uea4io

What's next:
    View a summary of image vulnerabilities and recommendations → docker scout quickview 
[11:47:31] pierrelepottier :: Pierres-MacBook-Pro  ➜  docker-pierrelepottier/tp1/sample_app ‹main*› » docker login            
Authenticating with existing credentials... [Username: plepottier]

i Info → To login with a different account, run 'docker logout' followed by 'docker login'


Login Succeeded
[11:50:34] pierrelepottier :: Pierres-MacBook-Pro  ➜  docker-pierrelepottier/tp1/sample_app ‹main*› » docker tag pierre:latest plepottier/pierre:latest  
[11:52:17] pierrelepottier :: Pierres-MacBook-Pro  ➜  docker-pierrelepottier/tp1/sample_app ‹main*› » docker push plepottier/pierre:latest  
The push refers to repository [docker.io/plepottier/pierre]
016369aa6675: Pushed 
77cd157b7fe2: Pushed 
ebfb08d53d66: Pushed 
6b8428b7762d: Pushed 
ec3bc9c2d5b7: Pushed 
5f70bf18a086: Mounted from library/golang 
6fb2efea6c8f: Mounted from library/golang 
c63593ddc7d1: Mounted from library/golang 
c301b8e6e0f7: Mounted from library/golang 
20f026ae0a91: Mounted from library/golang 
f21c087a3964: Mounted from library/golang 
cedb364ef937: Mounted from library/golang 
latest: digest: sha256:f87366aa0c5ca495aaab62e1f18a8fdcf23cd09e5c1938b19183272535e0d34b size: 2833
[11:52:43] pierrelepottier :: Pierres-MacBook-Pro  ➜  docker-pierrelepottier/tp1/sample_app ‹main*› » 
```

> Le link : `https://hub.docker.com/repository/docker/plepottier/pierre/general`

# Part III. Compose

# I. Getting started

## 1. Run it

**Lancez les deux conteneurs** avec `docker compose`

- déplacez-vous dans le dossier `compose_test` qui contient le fichier `docker-compose.yml`
- go exécuter `docker compose up -d`

```bash
[11:57:45] pierrelepottier :: Pierres-MacBook-Pro  ➜  docker-pierrelepottier/tp1/compose_test ‹main*› » docker compose up -d
WARN[0000] /Users/pierrelepottier/IntelliJProjects/docker-pierrelepottier/tp1/compose_test/docker-compose.yml: the attribute `version` is obsolete, it will be ignored, please remove it to avoid potential confusion 
[+] Running 3/3
 ✔ Network compose_test_default                  C...                                0.0s 
 ✔ Container compose_test-conteneur_nul-1        Started                             0.1s 
 ✔ Container compose_test-conteneur_flopesque-1  Started                             0.1s 
[11:58:22] pierrelepottier :: Pierres-MacBook-Pro  ➜  docker-pierrelepottier/tp1/compose_test ‹main*› » 
```

**Vérifier que les deux conteneurs tournent**

- toujours avec une commande `docker`
- tu peux aussi use des trucs comme `docker compose ps` ou `docker compose top` qui sont cools dukoo
    - `docker compose --help` pour voir les bails

```bash
[11:58:22] pierrelepottier :: Pierres-MacBook-Pro  ➜  docker-pierrelepottier/tp1/compose_test ‹main*› » docker ps
CONTAINER ID   IMAGE     COMMAND        CREATED          STATUS          PORTS     NAMES
a9c72980a9f4   debian    "sleep 9999"   36 seconds ago   Up 35 seconds             compose_test-conteneur_nul-1
9a1cc529c6cb   debian    "sleep 9999"   36 seconds ago   Up 35 seconds             compose_test-conteneur_flopesque-1
[11:58:58] pierrelepottier :: Pierres-MacBook-Pro  ➜  docker-pierrelepottier/tp1/compose_test ‹main*› » docker compose ps
WARN[0000] /Users/pierrelepottier/IntelliJProjects/docker-pierrelepottier/tp1/compose_test/docker-compose.yml: the attribute `version` is obsolete, it will be ignored, please remove it to avoid potential confusion 
NAME                                 IMAGE     COMMAND        SERVICE               CREATED          STATUS          PORTS
compose_test-conteneur_flopesque-1   debian    "sleep 9999"   conteneur_flopesque   51 seconds ago   Up 50 seconds   
compose_test-conteneur_nul-1         debian    "sleep 9999"   conteneur_nul         51 seconds ago   Up 50 seconds   
[11:59:13] pierrelepottier :: Pierres-MacBook-Pro  ➜  docker-pierrelepottier/tp1/compose_test ‹main*› » docker compose top
WARN[0000] /Users/pierrelepottier/IntelliJProjects/docker-pierrelepottier/tp1/compose_test/docker-compose.yml: the attribute `version` is obsolete, it will be ignored, please remove it to avoid potential confusion 
SERVICE              #   UID   PID   PPID  C   STIME  TTY  TIME      CMD
conteneur_flopesque  1   root  2750  2706  0   09:58  ?    00:00:00  sleep 9999
conteneur_nul        1   root  2751  2705  0   09:58  ?    00:00:00  sleep 9999
[11:59:29] pierrelepottier :: Pierres-MacBook-Pro  ➜  docker-pierrelepottier/tp1/compose_test ‹main*› » 
```

## 2. What about networking

**Pop un shell dans le conteneur `conteneur_nul`**

- référez-vous au mémo Docker
- effectuez un `ping conteneur_flopesque` (ouais ouais, avec ce nom là)
    - un conteneur est aussi léger que possible, aucun programme/fichier superflu : t'auras pas la commande `ping` !
    - il faudra installer un paquet qui fournit la commande `ping` pour pouvoir tester
    - juste pour te faire remarquer que les conteneurs ont pas besoin de connaître leurs IP : les noms fonctionnent

```bash
[12:00:41] pierrelepottier :: Pierres-MacBook-Pro  ➜  docker-pierrelepottier/tp1/compose_test ‹main*› » docker exec -it compose_test-conteneur_nul-1 sh
# ping conteneur_flopesque
sh: 1: ping: not found
# apt-get update
Get:1 http://deb.debian.org/debian bookworm InRelease [151 kB]
Get:2 http://deb.debian.org/debian bookworm-updates InRelease [55.4 kB]
Get:3 http://deb.debian.org/debian-security bookworm-security InRelease [48.0 kB]
Get:4 http://deb.debian.org/debian bookworm/main arm64 Packages [8693 kB]
Get:5 http://deb.debian.org/debian bookworm-updates/main arm64 Packages [756 B]
Get:6 http://deb.debian.org/debian-security bookworm-security/main arm64 Packages [264 kB]
Fetched 9213 kB in 4s (2218 kB/s)                       
Reading package lists... Done
# apt-get install -y iputils-ping
Reading package lists... Done
Building dependency tree... Done
Reading state information... Done
The following additional packages will be installed:
libcap2-bin libpam-cap
The following NEW packages will be installed:
iputils-ping libcap2-bin libpam-cap
0 upgraded, 3 newly installed, 0 to remove and 0 not upgraded.
Need to get 94.9 kB of archives.
After this operation, 598 kB of additional disk space will be used.
Get:1 http://deb.debian.org/debian bookworm/main arm64 libcap2-bin arm64 1:2.66-4+deb12u1 [34.1 kB]
Get:2 http://deb.debian.org/debian bookworm/main arm64 iputils-ping arm64 3:20221126-1+deb12u1 [46.1 kB]
Get:3 http://deb.debian.org/debian bookworm/main arm64 libpam-cap arm64 1:2.66-4+deb12u1 [14.7 kB]
Fetched 94.9 kB in 0s (270 kB/s)       
debconf: delaying package configuration, since apt-utils is not installed
Selecting previously unselected package libcap2-bin.
(Reading database ... 6083 files and directories currently installed.)
Preparing to unpack .../libcap2-bin_1%3a2.66-4+deb12u1_arm64.deb ...
Unpacking libcap2-bin (1:2.66-4+deb12u1) ...
Selecting previously unselected package iputils-ping.
Preparing to unpack .../iputils-ping_3%3a20221126-1+deb12u1_arm64.deb ...
Unpacking iputils-ping (3:20221126-1+deb12u1) ...
Selecting previously unselected package libpam-cap:arm64.
Preparing to unpack .../libpam-cap_1%3a2.66-4+deb12u1_arm64.deb ...
Unpacking libpam-cap:arm64 (1:2.66-4+deb12u1) ...
Setting up libcap2-bin (1:2.66-4+deb12u1) ...
Setting up libpam-cap:arm64 (1:2.66-4+deb12u1) ...
debconf: unable to initialize frontend: Dialog
debconf: (No usable dialog-like program is installed, so the dialog based frontend cannot be used. at /usr/share/perl5/Debconf/FrontEnd/Dialog.pm line 78.)
debconf: falling back to frontend: Readline
debconf: unable to initialize frontend: Readline
debconf: (Can't locate Term/ReadLine.pm in @INC (you may need to install the Term::ReadLine module) (@INC contains: /etc/perl /usr/local/lib/aarch64-linux-gnu/perl/5.36.0 /usr/local/share/perl/5.36.0 /usr/lib/aarch64-linux-gnu/perl5/5.36 /usr/share/perl5 /usr/lib/aarch64-linux-gnu/perl-base /usr/lib/aarch64-linux-gnu/perl/5.36 /usr/share/perl/5.36 /usr/local/lib/site_perl) at /usr/share/perl5/Debconf/FrontEnd/Readline.pm line 7.)
debconf: falling back to frontend: Teletype
Setting up iputils-ping (3:20221126-1+deb12u1) ...
# ping conteneur_flopesque
PING conteneur_flopesque (172.18.0.2) 56(84) bytes of data.
64 bytes from compose_test-conteneur_flopesque-1.compose_test_default (172.18.0.2): icmp_seq=1 ttl=64 time=0.183 ms
64 bytes from compose_test-conteneur_flopesque-1.compose_test_default (172.18.0.2): icmp_seq=2 ttl=64 time=0.250 ms
64 bytes from compose_test-conteneur_flopesque-1.compose_test_default (172.18.0.2): icmp_seq=3 ttl=64 time=0.258 ms
64 bytes from compose_test-conteneur_flopesque-1.compose_test_default (172.18.0.2): icmp_seq=4 ttl=64 time=0.350 ms
64 bytes from compose_test-conteneur_flopesque-1.compose_test_default (172.18.0.2): icmp_seq=5 ttl=64 time=0.357 ms
^C
--- conteneur_flopesque ping statistics ---
5 packets transmitted, 5 received, 0% packet loss, time 4027ms
rtt min/avg/max/mdev = 0.183/0.279/0.357/0.065 ms
```

# II. A working meow-api

Bon, la `meow-api` elle throw des belles erreurs SQL quand on va sur une de ses (seules) routes comme `/users`.

Elle a besoin d'une database pour fonctionner.

## 6. Rendu attendu

**Un dossier `meow_compose/` dans votre dépôt git, qui contient :**

- le `docker-compose.yml`
- le fichier de seed SQL `seed.sql`
- le fichier d'environnement `.env`
- le `Dockerfile` pour build `meow-api`

**Dans votre README de rendu**

- un `docker compose up` qui fonctionne
- un `curl` sur l'API, sur la route `/users`
- un `curl` sur l'API, sur la route `/user/3`

```bash
[14:41:25] pierrelepottier :: Pierres-MacBook-Pro  ➜  docker-pierrelepottier/tp1/meow_compose ‹main*› » docker compose up -d --build     
Compose can now delegate builds to bake for better performance.
 To do so, set COMPOSE_BAKE=true.
[+] Building 0.9s (12/12) FINISHED                                   docker:desktop-linux
 => [meow-api internal] load build definition from Dockerfile                        0.0s
 => => transferring dockerfile: 596B                                                 0.0s
 => [meow-api internal] load metadata for docker.io/library/python:3                 0.8s
 => [meow-api auth] library/python:pull token for registry-1.docker.io               0.0s
 => [meow-api internal] load .dockerignore                                           0.0s
 => => transferring context: 2B                                                      0.0s
 => [meow-api 1/5] FROM docker.io/library/python:3@sha256:5f69d22a88dd4cc4ee1576def  0.0s
 => [meow-api internal] load build context                                           0.0s
 => => transferring context: 137B                                                    0.0s
 => CACHED [meow-api 2/5] WORKDIR /app                                               0.0s
 => CACHED [meow-api 3/5] COPY ./requirements.txt .                                  0.0s
 => CACHED [meow-api 4/5] RUN pip install --no-cache-dir -r requirements.txt         0.0s
 => CACHED [meow-api 5/5] COPY ./app.py .                                            0.0s
 => [meow-api] exporting to image                                                    0.0s
 => => exporting layers                                                              0.0s
 => => writing image sha256:b7062147ee6c7b7b485e23e8378e931a3895939ff8b0aa65299fe35  0.0s
 => => naming to docker.io/library/meow_compose-meow-api                             0.0s
 => [meow-api] resolving provenance for metadata file                                0.0s
[+] Running 4/4
 ✔ meow-api                      Built                                               0.0s 
 ✔ Network meow_compose_default  Created                                             0.0s 
 ✔ Container meow-db             Started                                             0.1s 
 ✔ Container meow-api            Started    
```

```bash
[14:41:35] pierrelepottier :: Pierres-MacBook-Pro  ➜  docker-pierrelepottier/tp1/meow_compose ‹main*› » curl http://localhost:8000/user/3
{"favorite_insult":"Stop paw-sing around!","id":3,"name":"Charlie"}
[14:41:40] pierrelepottier :: Pierres-MacBook-Pro  ➜  docker-pierrelepottier/tp1/meow_compose ‹main*› » curl http://localhost:8000/users 
[{"favorite_insult":"You silly cat!","id":1,"name":"Alice"},{"favorite_insult":"Meow you kidding me!","id":2,"name":"Bob"},{"favorite_insult":"Stop paw-sing around!","id":3,"name":"Charlie"},{"favorite_insult":"You fur-getful feline!","id":4,"name":"Diana"},{"favorite_insult":"Purr-haps think twice!","id":5,"name":"Eve"}]
[14:41:47] pierrelepottier :: Pierres-MacBook-Pro  ➜  docker-pierrelepottier/tp1/meow_compose ‹main*› »  
```
