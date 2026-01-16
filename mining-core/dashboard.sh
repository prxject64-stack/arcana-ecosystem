#!/bin/bash
SESSION="infinite_network"
tmux new-session -d -s $SESSION

# Create 8 panes for 8 Prover Nodes
tmux selectp -t 0
tmux splitw -h
tmux splitw -v
tmux selectp -t 0
tmux splitw -v
tmux selectp -t 2
tmux splitw -h
tmux selectp -t 4
tmux splitw -v
tmux selectp -t 6
tmux splitw -h

# Assign each pane to tail a specific node log
for i in {0..7}; do
    NODE=$((i+1))
    tmux send-keys -t $i "tail -f node_0$NODE.log" C-m
done

tmux attach-session -t $SESSION
