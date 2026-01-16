# ORIGIN: ARCANA-CORE BUILD COMMANDS
These commands were used to resolve the complex static link chains for the core engine.

- **Dependency Install**: `apt-get install -y libsodium-dev libtinfo-dev libncurses5-dev` 
- **Environment Reset**: `cd /Arcana-core/engine/build && rm -rf *` [cite: 1, 5]
- **Forced Static Configuration**: 
  ```bash
  cmake -DSTATIC=ON -DMANUAL_SUBMODULES=1 -DENABLE_PGM=OFF -DUSE_DEVICE_TREZOR=OFF -DBUILD_TESTS=OFF -DEXTERNAL_UNBOUND=ON -DCMAKE_C_COMPILER_WORKS=1 -DCMAKE_CXX_COMPILER_WORKS=1 ..
  ``` 
- **Build Execution**: `make -j$(nproc)` [cite: 1, 5]
