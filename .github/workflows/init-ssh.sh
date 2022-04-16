SSH_PRIVATE_KEY="$1"
SSH_KNOWN_HOSTS="$2"
test -n "$SSH_PRIVATE_KEY" || ( echo "missing variable SSH_PRIVATE_KEY" && exit 1)
test -n "$SSH_KNOWN_HOSTS" || ( echo "missing variable SSH_KNOWN_HOSTS" && exit 1)
which ssh-agent || ( apt-get update -y && apt-get install openssh-client -y )
eval $(ssh-agent -s)
echo "$SSH_PRIVATE_KEY" | tr -d '\r' | ssh-add - > /dev/null
mkdir -p ~/.ssh
chmod 700 ~/.ssh
ssh-keyscan -H "$SSH_KNOWN_HOSTS" > ~/.ssh/known_hosts
chmod 644 ~/.ssh/known_hosts