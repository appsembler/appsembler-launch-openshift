Appsembler launch widget quickstart for OpenShift
=================================================

The Appsembler launch widget provides a convenient way to quickly deploy open source web applications to evaluate them. Currently, there is support for [Redhat's OpenShift PaaS](http://openshift.com).

Deploying to OpenShift
----------------------

In order to set all the environment variables correctly, you need to copy the file::

```
$ cd .openshift/action_hooks
$ cp pre_start_python.tmpl pre_start_python
```

And then edit this file with all of the correct values for your Mandrill, Redis, Sentry, Pusher and OpenShift accounts. 

Then to deploy run these commands:

```
$ rhc app create myappsemblerlaunch -t python-2.6 --nogit
$ git remote add openshift ssh://xxx@myappsemblerlaunch-domain.rhcloud.com/~/git/myappsemblerlaunch.git/
$ git push openshift master
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
