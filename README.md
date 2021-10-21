## prepara dev env
```sh
virtualenv env
source env/bin/activate

pip3 install kserve

# pip3 install ray[default]
# pip3 install ray[serve] --no-cache-dir
pip3 freeze > requirements.txt
```
## build with buildpack and push
```sh
export DOCKER_USER=arllanos

pack build --builder=heroku/buildpacks:20 ${DOCKER_USER}/custom-model:v2
docker push ${DOCKER_USER}/custom-model:v2

```
## deploy inference
```sh
cat << EOF > custom.yaml
apiVersion: serving.kserve.io/v1beta1
kind: InferenceService
metadata:
  name: custom-model
spec:
  predictor:
    containers:
      - name: kserve-container
        image: ${DOCKER_USER}/custom-model:v1
EOF

kubectl apply -f custom.yaml
```