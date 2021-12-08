import tonos_ts4.ts4 as ts4

eq = ts4.eq

ts4.init('./', verbose = True)
VENDORING_PATH='../../../vendoring/'

#deploy
keypair = ts4.make_keypair()
setcodemultisig = ts4.BaseContract(VENDORING_PATH + 'setcodemultisig/SetcodeMultisigWallet', ctor_params = {'owners': [keypair[1]], 'reqConfirms': 1}, keypair = keypair)

codeIndex = ts4.load_code_cell(VENDORING_PATH + 'compiled/Index.tvc')
codeData = ts4.load_code_cell(VENDORING_PATH + 'compiled/Data.tvc')

print (keypair[1])

# 5465737420636f6c6c656374696f6e (in hex) = Test collection
collectionName = "5465737420636f6c6c656374696f6e"
# 4465736372697074696f6e = Description
collectionDescription = "4465736372697074696f6e" 
editionAmount = 10
nftRoot = ts4.BaseContract('compiled/NftRoot', ctor_params = {'codeIndex': codeIndex, 'codeData': codeData, 'ownerPubkey': keypair[1], 'collectionName': collectionName, 'collectionDescription': collectionDescription, 'editionAmount': editionAmount}, keypair = keypair)

ts4.dispatch_messages()

#id
IRequiredInterfaces = 1
ICollectable = 2
ReqInterfaces = [IRequiredInterfaces, ICollectable]

answReqInterfaces = nftRoot.call_getter('getRequiredInterfaces')
answColInfo = nftRoot.call_getter('getCollectionInfo')

assert eq(answColInfo[0], collectionName)
assert eq(answColInfo[1], collectionDescription)
assert eq(answColInfo[2], editionAmount)
assert eq(answReqInterfaces, ReqInterfaces)