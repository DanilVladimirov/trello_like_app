### запуск проекту

```shell
  docker-compose up -d --build
```

після запуску проекту, створються тестові юзери і тестова задача.


user_id1 = 7725640d-477a-45d6-b0ce-3d1c905426f1

user_id2 = 7725640d-477a-45d6-b0ce-3d1c905426f1

task_id = df176e79-a72f-44f4-b0bc-b4c2b205c83b

також авторизація описана поверхнево (по умовам задачі), тому при кожному запиті буде рахуватись що ви користувач 7725640d-477a-45d6-b0ce-3d1c905426f1


### приклад api запиту 

```shell
curl --location --request PUT '127.0.0.1:8002/tasks/df176e79-a72f-44f4-b0bc-b4c2b205c83b' \
--header 'Authorization: Bearer gewgewgeg' \
--header 'Content-Type: application/json' \
--data '{
    "name": "gewgsfasfsafsafafaf fas af wge",
    "description": "t12e12st",
    "owner_id": "7725640d-477a-45d6-b0ce-3d1c905426f1",
    "user_ids": [
        "7725640d-477a-45d6-b0ce-3d1c905426f1"
    ],
    "status": "Done"
}'
```
