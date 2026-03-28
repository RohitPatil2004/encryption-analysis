#!/bin/bash
# experiments/run_e2e_highload.sh  -  Member 1
# E2E high-load: 100 parallel streams, 60 sec, 3 runs per hop count
# Usage: sudo bash experiments/run_e2e_highload.sh
 
set -e
PARALLEL=100 ; DURATION=60 ; RUNS=3 ; ENC_TYPE="e2e"
LOG_DIR="analysis/results"
mkdir -p "$LOG_DIR"
 
for HOPS_COUNT in 2 4 6; do
    case $HOPS_COUNT in
        2) DEST_IP="10.0.0.3" ;;
        4) DEST_IP="10.0.0.5" ;;
        6) DEST_IP="10.0.0.7" ;;
    esac
    for RUN in $(seq 1 $RUNS); do
        SCENARIO="${HOPS_COUNT}hop_highload_run${RUN}"
        echo "--- $SCENARIO ($ENC_TYPE) ---"
        iperf3 -c "$DEST_IP" -P "$PARALLEL" -t "$DURATION" -J \
               --logfile "$LOG_DIR/iperf3_${ENC_TYPE}_${SCENARIO}.json"
        sleep 3
    done
done
echo "Done. Results in $LOG_DIR/"
