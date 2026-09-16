@echo off
REM GIT_ASKPASS helper: git calls this with the prompt text as %1.
REM We answer from the environment so no secret is ever written to disk
REM or printed to the terminal.
echo(%GH_TOKEN_FOR_GIT%
