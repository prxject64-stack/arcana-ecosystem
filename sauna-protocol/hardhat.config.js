require('@nomicfoundation/hardhat-toolbox');

task('dashboard').setAction(async(a,hre)=>{
  const CC='0xe7f1725E7734CE288F8367e1Bb143E90bb3F0512';
  const SUSD='0x84eA74d481Ee0A5332c457a4d796187F6Ba67fEB';
  const TR='0x322813fd9a05da47206818293028c39ed8b00000';
  const SMM='0x18E317A7D70d8fBf8e6E893616b52390EbBdb629';
  const cc=await hre.ethers.getContractAt('contracts/IERC20.sol:IERC20',CC);
  const ss=await hre.ethers.getContractAt('contracts/IERC20.sol:IERC20',SUSD);
  const d=[
    {E:'Treasury',C:await cc.balanceOf(TR),S:await ss.balanceOf(TR)},
    {E:'SMM',C:await cc.balanceOf(SMM),S:await ss.balanceOf(SMM)}
  ];
  console.table(d.map(r=>({Entity:r.E,CC:hre.ethers.formatUnits(r.C,18),sUSD:hre.ethers.formatUnits(r.S,18)})));
});

task('balance').addParam('account').setAction(async(a,h)=>{
  const t=await h.ethers.getContractAt('contracts/IERC20.sol:IERC20','0xe7f1725E7734CE288F8367e1Bb143E90bb3F0512');
  const b=await t.balanceOf(a.account);
  console.log('Balance of ' + a.account + ': ' + h.ethers.formatUnits(b, 18) + ' CC');
});

module.exports={solidity:'0.8.33',networks:{localhost:{url:'http://127.0.0.1:8545'}}};
