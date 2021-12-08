pragma ton-solidity = 0.47.0;

interface ITags {
    function getTags() external returns (string[] tags);
    function getTagsResponsible() external responsible returns (string[] tags);
}

library TagsLib {
    int constant ID = 4;        
}

abstract contract Tags is ITags {
    
    string[] _tags; 

    function getTags() external override returns (string[] tags) {
        return _tags;
    }

    function getTagsResponsible() public responsible override returns (string[]  ) {
        return {value: 0, flag: 64}(_tags);
    }
}