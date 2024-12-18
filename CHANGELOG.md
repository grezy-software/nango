# [1.1.0](https://github.com/grezy-software/nango/compare/v1.0.1...v1.1.0) (2024-11-09)


### Bug Fixes

* **.envs:** fix variables & logs for envs files generator ([014ccd6](https://github.com/grezy-software/nango/commit/014ccd638f5dfbc8a1cf6364f4e1b7c68add1cfb))
* **ci:** removed imports in __init__.py ([3f08474](https://github.com/grezy-software/nango/commit/3f084748e686469a1a31efbb70998ea8c2050bca))
* **ci:** up-prod ([f30d3b3](https://github.com/grezy-software/nango/commit/f30d3b3d3bfc343883c5c3acf6ca7d5544904b04))
* **drf:** DEFAULT_SCHEMA_CLASS only in dev mode ([862c1d3](https://github.com/grezy-software/nango/commit/862c1d3b5dcbdc6cb41dc0ffba0009ef913865c6))
* **readme:** remove todo list from readme ([ee413dd](https://github.com/grezy-software/nango/commit/ee413ddc7de044a5925df7e7bfb383edc57dd86b))
* **requirement:** add gunicorn ([fab8ecf](https://github.com/grezy-software/nango/commit/fab8ecffe78121b30119459991edda3148223cc9))
* **type_factory:** corrected Date type to string ([ba15bef](https://github.com/grezy-software/nango/commit/ba15bef1e89f4cf7509b01d2c97f33586bd87844))
* **type_factory:** ListField & MethodField ([12d9f29](https://github.com/grezy-software/nango/commit/12d9f290c48fa421a22a68827ed2175521bb6e2d))
* **werkzeug:** stop the reload from going crazy ([6f86ca0](https://github.com/grezy-software/nango/commit/6f86ca0ff19243ff74c303e74c13a1ed8d7eab26))


### Features

* **frontend:** useMounted ([18833cd](https://github.com/grezy-software/nango/commit/18833cd16cbaa3742629e4494bab17084b0a23b4))

## [1.0.1](https://github.com/grezy-software/nango/compare/v1.0.0...v1.0.1) (2024-10-30)


### Bug Fixes

* **bridge:** circular imports ([b867981](https://github.com/grezy-software/nango/commit/b867981c73925453ce5f4c933d40cf0f5aca5236))

# 1.0.0 (2024-10-23)


### Features

* **init:** first commit ([582b26f](https://github.com/grezy-software/nango/commit/582b26f8bf2e60742ab88ab1f9d3f1c78e3c9e4e))

# 1.0.0 (2024-10-22)


### Bug Fixes

* **.envs:** remove `\` from fernet generated keys ([69058ff](https://github.com/grezy-software/nango/commit/69058ff324975301fe70c244386738a4accb01e1))
* **.envs:** Remove misplaced quotes ([8e5bf55](https://github.com/grezy-software/nango/commit/8e5bf5554710f61e3edeaec2dde4dc68b63764d7))
* **api:** improve API error message ([10876d7](https://github.com/grezy-software/nango/commit/10876d7cb4d69fcc9255a21b98773d0afd7438bd))
* **bridge:** change name & fix other bugs ([84adedf](https://github.com/grezy-software/nango/commit/84adedfcf63129b926bdff772aee073dc772240f))
* **bridge:** dynamic fields for serializer generation now only work for nango managed fields ([67534bc](https://github.com/grezy-software/nango/commit/67534bce7799b4ac7068cf110832289f007795cf))
* **bridge:** minor fixes on new bridge ([784bae6](https://github.com/grezy-software/nango/commit/784bae6c18c41481a701a86390a62848244bf337))
* **bridge:** solve import issue on bridge ([dae026c](https://github.com/grezy-software/nango/commit/dae026c8e240ca35811916581eb292a2fe6bcaa7))
* **ci:** up-prod ([801a1da](https://github.com/grezy-software/nango/commit/801a1da70f8a2cfca4d6473eafd31d0dc05437c4))
* **ci:** up-prod ([75b5869](https://github.com/grezy-software/nango/commit/75b5869cf7804d879ae96b68fd62458310e66c86))
* **ci:** up-prod ([f9cfdf5](https://github.com/grezy-software/nango/commit/f9cfdf537acfe6833f7a520942ef9a1e1b1b54cd))
* **ci:** up-prod ([98fd5f8](https://github.com/grezy-software/nango/commit/98fd5f81e5e2ca2fc4fa0bf6e37c9f8f2a58863c))
* **ci:** up-prod ([6a59adb](https://github.com/grezy-software/nango/commit/6a59adbb8419ce6475961e2f0563d4ef3ff649e5))
* **ci:** up-prod ([9e1eac3](https://github.com/grezy-software/nango/commit/9e1eac3db77234f3b81639e1682ceef238cc3101))
* **ci:** up-prod ([5ecdbf5](https://github.com/grezy-software/nango/commit/5ecdbf536bdde3bea69099ac46d20711fcfbe599))
* **docker:** add node_modules installations in nextjs' dockerfile ([ec6b5ab](https://github.com/grezy-software/nango/commit/ec6b5ab204b926a2a73c862f4c3a20893675ac9b))
* **docker:** fix anchor issue on development-postgres.yml docker compose file ([76a7141](https://github.com/grezy-software/nango/commit/76a71412ef40504981a6f3bb0ef7f9e00b07736c))
* **docker:** mkdocs works now on docker compose ([1109212](https://github.com/grezy-software/nango/commit/1109212704af677c2443cc167617742bbfe09594))
* **env_file_generator:** cannot overwrite existing .env files ([c79f1bf](https://github.com/grezy-software/nango/commit/c79f1bfb7b5d345a631008ed95c86e4c03115024))
* **env:** add DJANGO_SETTINGS_MODULE to env_file_generator ([cc0e67d](https://github.com/grezy-software/nango/commit/cc0e67d05be312ef84a21c364eaedae83b2fb198))
* **message:** fix message's endpoints' permissions & auth ([3dce989](https://github.com/grezy-software/nango/commit/3dce989581a2117b62601e182c467e1d109a3ad2))
* **nango:** Bridge.get_model method check model's nango's settings to build the list of models ([8e77de9](https://github.com/grezy-software/nango/commit/8e77de9e3dae51d0ece5f5e667a0f9fa3ac5de90))
* **nango:** celery & django crash ([3e9ae12](https://github.com/grezy-software/nango/commit/3e9ae1217c352918127700a2b8a5b24d6029c8b2))
* **nango:** change generated imports for custom serializer to avoid circular imports ([50f5752](https://github.com/grezy-software/nango/commit/50f5752c8ed84e8e0733a7c20faaa6db11b4d33d))
* **nango:** change generated imports for custom serializer to avoid circular imports ([cefa0ee](https://github.com/grezy-software/nango/commit/cefa0ee778c436def405be9d3714c12b5f7d93f2))
* **nango:** improve from CamelCase to snake_case convertion ([63816bf](https://github.com/grezy-software/nango/commit/63816bfcd2eadb400e5e63fd395270a92fd48ac5))
* **nango:** improveme template ([a4540a3](https://github.com/grezy-software/nango/commit/a4540a3779da855034cd580b6beaa07a48bd2995))
* **nango:** modifications about model_name management in nango's bridge ([72bd657](https://github.com/grezy-software/nango/commit/72bd65702c2894e2177b7775ace32b91dcf54e95))
* **nango:** related_field are now removed from serializer selected fields if the model is not model managed ([85c8713](https://github.com/grezy-software/nango/commit/85c87131efb78c1df7ab8eee1156732deb3f5c41))
* **nango:** remove useless import from template generation ([d3d74f6](https://github.com/grezy-software/nango/commit/d3d74f61afc3c1e072b31dbcb3ab9562213feffa))
* **postgres:** changed :latest into :17 to avoid breaking on new releases ([b372653](https://github.com/grezy-software/nango/commit/b3726533583f4868116a175830d5364a39c0fb93))
* **readme:** typo ([3680fef](https://github.com/grezy-software/nango/commit/3680fef330f649e972782e9004a89958506ff497))
* **ruff:** fix pre-commit hook ([2557a4e](https://github.com/grezy-software/nango/commit/2557a4e3eb9111b397d6d0cc59f1a99c575f8a06))
* **semantic:** add .releaserc ([3004f7a](https://github.com/grezy-software/nango/commit/3004f7a0f5758e94762f9189ccdfd02045c564c3))
* **settings:** improve settings ([2099244](https://github.com/grezy-software/nango/commit/20992447d528fc622527627c7e833eff1e1667a3))
* **setup:** fix dependabot ([52a009b](https://github.com/grezy-software/nango/commit/52a009bf38c69037974123785b118b967e3a5ef8))
* **tmp:** working on CI ([7142d60](https://github.com/grezy-software/nango/commit/7142d606224a83cf656b5004979816e4b5b52f2e))
* **tmp:** working on CI ([9301529](https://github.com/grezy-software/nango/commit/9301529e5abfa2ef090d5e1fddb84acd9190997b))
* **user:** frontend for user creation ([26cc9b5](https://github.com/grezy-software/nango/commit/26cc9b5db2c9801473d0156a06779d3cf177e693))


### Features

* **bridge:** add base settings for the bridge ([eb6896a](https://github.com/grezy-software/nango/commit/eb6896a122da2031c4cf23facb77bc7a47d6a2b0))
* **bridge:** add CLI command to run the bridge ([a4755d3](https://github.com/grezy-software/nango/commit/a4755d3706469a0ff08b20d9af9150a58742350c))
* **bridge:** add default configuration to the bridge ([0c1b4f9](https://github.com/grezy-software/nango/commit/0c1b4f94cdb6c15df7840de2a092629ab2564b0a))
* **bridge:** add dynamic url routing ([0567c05](https://github.com/grezy-software/nango/commit/0567c057ba4534a98af6eb7cc76512f9ebf92904))
* **bridge:** add static files ([1dfcb21](https://github.com/grezy-software/nango/commit/1dfcb2122f8718ffa1665d9a01f8bdd9df6df316))
* **bridge:** add type generation (not implemented in bridge itself) ([fea6d04](https://github.com/grezy-software/nango/commit/fea6d04a452f2867ddd419940c313dcd6cad2887))
* **bridge:** serializers & views generation based on django's models ([1eebc10](https://github.com/grezy-software/nango/commit/1eebc104255650a0f59a43b7ebae6540f39a7ced))
* **config:** finish base config ([c624436](https://github.com/grezy-software/nango/commit/c624436a009ba0d9f31855bbb9a5f68871e11775))
* **docs:** docs' basement is ready ([23228cf](https://github.com/grezy-software/nango/commit/23228cf40d7b776904cbf3e94c66c811008c32d7))
* **frontend:** add base project for frontend ([a0c590e](https://github.com/grezy-software/nango/commit/a0c590e6ae2cf107bebaf60755db8b14dd183db0))
* **migration:** done migrating from Hugo ([9f7fbe4](https://github.com/grezy-software/nango/commit/9f7fbe4bbab5378df1d7605cf3b465abcdf7a487))
* **nango:** add authenticator to view's template ([3d545cb](https://github.com/grezy-software/nango/commit/3d545cb6c82e81812d9c0883341f3fbbb8d39df8))
* **nango:** add authenticator to view's template ([aa0b61a](https://github.com/grezy-software/nango/commit/aa0b61a12d17710aa6463b5ad9e053ccc4637587))
* **nango:** add jwt authentification ([759cedf](https://github.com/grezy-software/nango/commit/759cedf9235770f40b78a0f517650131efd9d32f))
* **nango:** add jwt authentification ([d01ce5d](https://github.com/grezy-software/nango/commit/d01ce5d67214f6b874d995b98dd100f8ab51271c))
* **nango:** add message model ([5478baf](https://github.com/grezy-software/nango/commit/5478baf6278703c4d093a9798d0a90a7593adb40))
* **nango:** command to display API routes ([f4bb4c9](https://github.com/grezy-software/nango/commit/f4bb4c96ded9b3435df47ff8c766108633b82a1e))
* **nango:** end of type generator ([697c709](https://github.com/grezy-software/nango/commit/697c709723d39a27994dda3a3a9753aea5973aa9))
* **ruff:** addpre-commit config ([9a06e35](https://github.com/grezy-software/nango/commit/9a06e35cad7d489129174f05de6d41cc0f73a90f))
* **settings:** base settings ([e0bdbfd](https://github.com/grezy-software/nango/commit/e0bdbfd749bf0533b309d20bbe1b46264fabda29))
* **setting:** setup base settings ([35ca430](https://github.com/grezy-software/nango/commit/35ca43021afc78bd76e527f6a8989d7b7209ceb4))
* **setting:** setup celery ([c62238c](https://github.com/grezy-software/nango/commit/c62238c83606c952c1e4676bd250f84db0448736))
* **setup:** .env load global environ varialbes ([1b215d1](https://github.com/grezy-software/nango/commit/1b215d1a47a474f71c3b330f0db506fc9479d53f))
* **stripe:** add stripe ([887c6e5](https://github.com/grezy-software/nango/commit/887c6e53bc7f3e11e9fd947962deed1da3009155))
* **types:** add base of AbstractTYpeFactory & AbstractType ([2c13e9c](https://github.com/grezy-software/nango/commit/2c13e9c1464e093a75928786da7d24732929a9e4))
* **url:** wip ([4c8df51](https://github.com/grezy-software/nango/commit/4c8df51752bbfe9428359ea5d9306006cc23005e))
* **user:** add update & destroy endpoints ([68fb3d2](https://github.com/grezy-software/nango/commit/68fb3d25f67262ff30c186ded2539317dc4e6526))
