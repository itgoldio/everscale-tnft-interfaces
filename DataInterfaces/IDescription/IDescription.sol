pragma ton-solidity = 0.47.0;

interface IDescription {
    function getDescription() external returns (string dataDescription);
    function getDescriptionResponsible() external responsible returns (string dataDescription);
}

library DescriptionLib {
    int constant ID = 3;        
}

abstract contract Description is IDescription {
    
    string _dataDescription;

    function getDescription() external override returns (string dataDescription) {
        return _dataDescription; 
    }

    function getDescriptionResponsible() external override responsible returns (string dataDescription) {
        return {value: 0, flag: 64}(_dataDescription);
    }

}