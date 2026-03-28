#!/bin/bash
# experiments/run_e2e_lowload.sh  -  Member 1
# Low-load: 10 parallel iperf3 streams, 30 sec, 3 runs per hop count
# Usage: sudo bash experiments/run_e2e_lowload.sh
 
set -e
PARALLEL=10 ; DURATION=30 ; RUNS=3 ; ENC_TYPE="e2e"
LOG_DIR="analysis/results"
mkdir -p "$LOG_DIR"
 
for HOPS_COUNT in 2 4 6; do
    case $HOPS_COUNT in
        2) DEST_IP="10.0.0.3" ;;
        4) DEST_IP="10.0.0.5" ;;
        6) DEST_IP="10.0.0.7" ;;
    esac
    for RUN in $(seq 1 $RUNS); do
        SCENARIO="${HOPS_COUNT}hop_lowload_run${RUN}"
        echo "--- $SCENARIO ($ENC_TYPE) ---"
        iperf3 -c "$DEST_IP" -P "$PARALLEL" -t "$DURATION" -J \
               --logfile "$LOG_DIR/iperf3_${ENC_TYPE}_${SCENARIO}.json"
        sleep 2
    done
done
echo "Done. Results in $LOG_DIR/"
