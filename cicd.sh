deploy_lambda_function() {
  local account_id="$1"
  local lambda_role="$2"
  local lambda_function_name="$3"

  aws lambda create-function \
    --function-name $lambda_function_name \
    --runtime python3.10 \
    --role $lambda_role \
    --handler
}

get_iam_role() {
  local role_name="$1"
  role_info=$(aws iam get-role --role-name "$role_name")
  if [ -z "$role_info" ]; then
    echo "IAM Role '$role_name' not found!"
    exit 1
  fi
}