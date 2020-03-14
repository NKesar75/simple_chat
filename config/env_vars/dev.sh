#!/usr/bin/env bash

# Main
# --------------------------------------------------------------------------------------------------
export PYTHONHASHSEED=0
export OUTPUT_PATH=./output


# DB info
# --------------------------------------------------------------------------------------------------
export DB_USER=postgres
export DB_PASSWORD=mctest
export DB_NAME=dalsimdb
export DB_PORT=5432
export DB_HOST=localhost


# simple chat
# --------------------------------------------------------------------------------------------------
export APP_NAME=simple_chat_service
export APP_SHORT_NAME=simple_chat
export APP_VERSION=0.1.0
export ENV=dev
export FLASK_ENV=development
export FLASK_APP=simple_chat/app.py
export FLASK_PORT=5000
