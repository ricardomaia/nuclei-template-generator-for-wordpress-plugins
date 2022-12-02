# Nuclei template generator for WordPress plugins

![GitHub issues](https://img.shields.io/github/issues/ricardomaia/nuclei-template-generator-for-wordpress-plugins) ![GitHub closed issues](https://img.shields.io/github/issues-closed-raw/ricardomaia/nuclei-template-generator-for-wordpress-plugins) ![GitHub release (latest by date)](https://img.shields.io/github/v/release/ricardomaia/nuclei-template-generator-for-wordpress-plugins) [![🛠 Template Validate](https://github.com/ricardomaia/nuclei-template-generator-for-wordpress-plugins/actions/workflows/template-validate.yml/badge.svg)](https://github.com/ricardomaia/nuclei-template-generator-for-wordpress-plugins/actions/workflows/template-validate.yml) [![❄️ YAML Lint](https://github.com/ricardomaia/nuclei-template-generator-for-wordpress-plugins/actions/workflows/syntax-checking.yml/badge.svg)](https://github.com/ricardomaia/nuclei-template-generator-for-wordpress-plugins/actions/workflows/syntax-checking.yml)

This is a simple script to scrape plugins from the WordPress website and then use to generate Nuclei templates.

![image](https://user-images.githubusercontent.com/1353811/205188352-090ff901-3a62-4654-a012-04059d7e7f3f.png)


## Generate or update templates

(Windows)
```console
docker compose up -d
```

(Linux)
```console
docker-compose up -d
```

## Run templates

### One target
```console
nuclei -t templates/technologies/wordpress -u https://www.example.com
```

### Multiple targets
```console
nuclei -t templates/technologies/wordpress -l list_of_targets.txt
```

![image](https://user-images.githubusercontent.com/1353811/205186958-af7b2d56-e6e4-4ff9-8b08-7cede4cd4908.png)
