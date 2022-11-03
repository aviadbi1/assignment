#!/bin/bash


run_moto() {
  /usr/local/bin/moto_server -H 0.0.0.0 -p 4000 &
}

create_ap_southeast() {
  for i in {1..20}; do
    aws ec2 run-instances \
      --endpoint-url=http://127.0.0.1:4000 \
      --image-id ami \
      --count 1 \
      --instance-type m5.2xlarge \
      --key-name test \
      --region=ap-southeast-1 2>&1 > /dev/null
    sleep 2
  done
}

create_eu_west() {
  for i in {1..20}; do
    aws ec2 run-instances \
      --endpoint-url=http://127.0.0.1:4000 \
      --image-id ami \
      --count 1 \
      --instance-type g5.16xlarge \
      --key-name test \
      --region=eu-west-1 2>&1 > /dev/null
    sleep 2
  done

}

create_us_east() {
  for i in {1..20}; do
    sleep 2
    aws ec2 run-instances \
      --endpoint-url=http://127.0.0.1:4000 \
      --image-id ami \
      --count 1 \
      --instance-type c6gd.medium \
      --key-name test \
      --region=us-east-1 2>&1 > /dev/null
  done
}

create_ec2_instances() {
  create_ap_southeast &
  create_eu_west &
  create_us_east &
}

main() {
  run_moto
  create_ec2_instances
  tail -f /dev/null
}

main
