# Nango

NextJs & Django had a baby! It's Nango!

This blueprint under steroids speeds up the development of your full stack application by providing a ready-to-use template and automatically builds the bridge between the frontend & backend.

The bridge contains:

- drf serializers
- drf endpoints
- backend routes
- front types
- api call methods

The workflow is simple:

1. Create a model in your backend
2. Run the `make bridge` command
3. Import type and api call methods in your frontend

## Activity

![Alt](https://repobeats.axiom.co/api/embed/3697d98ced5eddd922d97cdc1b47ecbc46b5f23c.svg "Repobeats analytics image")

##  Prerequisites

###  Env variables

Database:

- POSTGRES_USER
- POSTGRES_PASSWORD

Django:

- DJANGO_SECRET_KEY

Celery:

- CELERY_FLOWER_USER (optional)
- CELERY_FLOWER_PASSWORD (optional)

Stripe:

- STRIPE_PUBLISHABLE_KEY
- STRIPE_SECRET_KEY
- STRIPE_ENDPOINT_SECRET (optional)

Other:

- FRONTEND_URL (optional)

### Add node modules

To add a node module with `npx`, please ensure to add your module to the `./frontend`'s `package.json` file and not to the `/`'s `package.json`.

## Todo

### Blue print

- Django
  - [x] Structure
  - [x] Settings
    - [x] envs files generator
  - [x] Ruff
  - [x] Requirements
  - [x] Celery
  - [ ] API
    - [x] Structure
    - [x] Libraries
    - [ ] JWT
- NextJs
  - [x] Structure
  - [ ] Tailwind
  - [ ] Typescript
  - [ ] Eslint
  - [ ] Shadcn

- Github
  - [x] Dependabot (front & back)
  - [ ] CI (Tests, Lint, Build, Coverage)
  - [x] Pre-commit hook (ruff)

- Docker
  - Development
    - [ ] postgres
    - [ ] litestream
  - Production
    - [ ] postgres
    - [ ] litestream
    (content: postgres / litestream, redis, traefik, celery (worker, beat), flower, django, mkdocs, nextjs)

- [x] Semantic release
- [x] Mkdocs

### Bridge

- Backend
  - [ ] View Generator
  - [x] Serializer Generator
    - [x] Dynamic fields from models
    - [ ] Detail serializer
    - Handle nested models for detail serializer
      - [ ] ForeignKey
      - [ ] ManyToMany
      - [ ] OneToOne
    - [ ] Chirurgical edit on fields
  - [ ] Dynamic routes
  - [ ] Retrieve types from models
  - [ ] Progress bar

- Frontend
  - [ ] API call methods generator
  - [ ] Types generator

### Setup a new git repo

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
