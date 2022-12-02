# Nuclei template generator for WordPress plugins

This is a simple script to scrape plugins from the WordPress website and then use to generate Nuclei templates.

![image](https://user-images.githubusercontent.com/1353811/205187743-b1ca14c2-57be-4e12-a49d-ef6fb7281ec8.png)

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
