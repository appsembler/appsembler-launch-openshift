Appsembler launch widget quickstart for OpenShift
=================================================

The Appsembler launch widget provides a convenient way to quickly deploy open source web applications to evaluate them. Currently, there is support for [Redhat's OpenShift PaaS](http://openshift.com).

# Deploying to OpenShift
You need a working account for Mandrill, Sentry, Pusher and OpenShift for the app to work. You'll enter the account info in secret_keys file (step 7).

1. Create a new app: `rhc app create <app_name> python-2.6`
2. Add a redis cartridge to it: `rhc add-cartridge http://cartreflect-claytondev.rhcloud.com/reflect\?github\=smarterclayton/openshift-redis-cart -a <app_name>`
3. Go into the repo folder: `cd <app_name>`
4. Add this repo as upstream: `git remote add upstream https://github.com/appsembler/appsembler-launch-openshift.git`
5. Get the contents of this repo: `git pull -X theirs upstream master`
6. Run `rhc app show <app_name>`and copy the SSH URL
7. Edit the secret_keys file in the data/ folder and scp it to the server: `scp data/secret_keys <ssh_url>:app-root/data`
8. Push the data to the server: `git push`


## Setting up Sentry on Openshift
1. Please use the instructions on [Sentry quickstart](https://github.com/zemanel/openshift-sentry-quickstart) page.
2. Once you create a new project in Sentry, on the Project Details/Client Security page add rhcloud.com domain to the allowed domains.
3. From the project API Keys page, copy the full URL and set it as a `SENTRY_DSN` env variable on your Appsembler Launch project - preferably in the secret keys file you set up earlier.

## Running Flower monitoring system
To access Flower instance running on Appsembler Launch, type the following command in your shell: `rhc port-forward <app_name>` and access Flower through the browser on the address **127.0.0.1:5445**


Setting up New Relic for performance monitoring
-----------------------------------------------

Sign up for a New Relic account and find your license key. Install the newrelic package in your virtualenv:

```
$ pip install newrelic
```

Now run this command to generate a newrelic.ini file:

```
$ newrelic-admin generate-config <your-license-key> newrelic.ini
```

Troubleshooting
---------------

View the logs with:

```
$ rhc tail myappsemblerlaunch
```

You can also SSH into the container and debug with these commands:

```
$ rhc ssh myappsemblerlaunch
$ source python/virtenv/bin/activate
(virtenv)$ gear postreceive --trace
```

Migrate existing app
--------------------

In case you need to move the app to another Openshift account or recreate it, here's what needs to be done (note that the app name has to stay the same through all the steps):

1. `rhc snapshot save <app_name> -f <output_file>`
2. log in to the other account or delete the existing app (`rhc app delete <app_name>`)
3. `rhc app create <app_name> python-2.6 --no-git`
4. `rhc snapshot restore <app_name> -f <app_backup_file>`
5. wait a while
6. get the git repo url: `rhc app show <app_name>`
7. `git clone <git_repo_url>`
