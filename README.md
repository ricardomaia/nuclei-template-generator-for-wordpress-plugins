# Nuclei template generator for WordPress plugins

[![🛠 Template Validate](https://github.com/ricardomaia/nuclei-template-generator-for-wordpress-plugins/actions/workflows/template-validate.yml/badge.svg)](https://github.com/ricardomaia/nuclei-template-generator-for-wordpress-plugins/actions/workflows/template-validate.yml) [![❄️ YAML Lint](https://github.com/ricardomaia/nuclei-template-generator-for-wordpress-plugins/actions/workflows/syntax-checking.yml/badge.svg)](https://github.com/ricardomaia/nuclei-template-generator-for-wordpress-plugins/actions/workflows/syntax-checking.yml) [![✨ Update WordPress Plugin Templates](https://github.com/ricardomaia/nuclei-template-generator-for-wordpress-plugins/actions/workflows/update-wordpress-plugin-templates.yml/badge.svg)](https://github.com/ricardomaia/nuclei-template-generator-for-wordpress-plugins/actions/workflows/update-wordpress-plugin-templates.yml)

This is a simple script to scrape plugins from the WordPress website and then use to generate Nuclei templates.

![image](https://user-images.githubusercontent.com/1353811/205188352-090ff901-3a62-4654-a012-04059d7e7f3f.png)

## Downloading templates

### With Nuclei

You can consume these Nuclei templates directly from GitHub.
Define the environment variable `GITHUB_TEMPLATE_REPO` like this:

```console
export GITHUB_TEMPLATE_REPO=ricardomaia/nuclei-template-generator-for-wordpress-plugins
```

Update templates

```console
$ nuclei -ut
                     __     _
   ____  __  _______/ /__  (_)
  / __ \/ / / / ___/ / _ \/ /
 / / / / /_/ / /__/ /  __/ /
/_/ /_/\__,_/\___/_/\___/_/   v2.8.1

                projectdiscovery.io

[INF] ricardomaia/nuclei-template-generator-for-wordpress-plugins: already up-to-date
[INF] No new updates found for nuclei templates
```

Using the templates

```console
nuclei -t github/nuclei-template-generator-for-wordpress-plugins/technologies/wordpress/plugins -u https://www.example.com
```

### Cloning this Repo

```console
$ git clone https://github.com/ricardomaia/nuclei-template-generator-for-wordpress-plugins.git
cd nuclei-template-generator-for-wordpress-plugin
```

With this option, you would run the templates as in the following examples.

## Run templates

### One target

```console
nuclei -t technologies/wordpress/plugins -u https://www.example.com
```

### One target & only TOP 100

```console
nuclei -ud ./nuclei-templates -t technologies/wordpress/plugins -tags top-100 -u https://www.example.com
```

### Multiple targets

```console
nuclei -ud ./nuclei-templates -t technologies/wordpress -l list_of_targets.txt
```

![image](https://user-images.githubusercontent.com/1353811/205873579-e92e61d0-f81f-4648-9216-5f1fa22168bb.png)

## Generate or update templates

(Windows)

```console
docker compose up -d
```

(Linux)

```console
docker-compose up -d
```

## Filtering JSON results

To get only outdated plugins.

```console
jq -r "select(.[\"matcher-name\"] != null) | .host, .info.metadata.plugin_namespace, .[\"extracted-results\"][], .[\"matcher-name\"], \"\n\" " < report.json
```

