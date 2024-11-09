# Nango

NextJs & Django had a baby! It's Nango!

This blueprint under steroids speeds up the development of your full stack application by providing a ready-to-use template and automatically builds the bridge between the frontend & backend.

The bridge contains:

- drf serializers
- drf endpoints
- backend routes
- front types
- api call methods (WIP)
- Tests (WIP)
- Scripts (for easy manual testing) (WIP)

## Activity

![Alt](https://repobeats.axiom.co/api/embed/3697d98ced5eddd922d97cdc1b47ecbc46b5f23c.svg "Repobeats analytics image")

## Setup a new git repo

Once you've created a new git repo from this template, we advise you enter the following command:

`git remote add nango git@github.com:grezy-software/nango.git`

If it worked, `git remote -v` should output:

```{bash}
nango git@github.com:grezy-software/nango.git (fetch)
nango git@github.com:grezy-software/nango.git (push)
origin git@github.com:grezy-projects/moguls.git (fetch)
origin git@github.com:grezy-projects/moguls.git (push)
```

Now, you can pull directly from nango to get all our latest updates by running `git pull nango main`.
If you have problems with pushing to the wrong remote, run: `git push -u origin <branch>` to set the upstream branch for the current checked out branch.

Otherwise, you can manually edit the git config with `git config --edit`

### Generate a token for AWS in order to prove private images

`echo -n "$USERNAME:$GH_TOKEN" | base64`

The GH_Token need the read:packages permission.
