import { buildModule } from "@nomicfoundation/hardhat-ignition/modules";

export default buildModule("SaunaModule", (m) => {
  const sauna = m.contract("SaunaStaking");

  return { sauna };
});
