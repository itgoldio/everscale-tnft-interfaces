import tonos_ts4.ts4 as ts4

eq = ts4.eq

ts4.init('./', verbose = True)
VENDORING_PATH='../../../vendoring/'

#deploy
keypair = ts4.make_keypair()
setcodemultisig = ts4.BaseContract(VENDORING_PATH + 'setcodemultisig/SetcodeMultisigWallet', ctor_params = {'owners': [keypair[1]], 'reqConfirms': 1}, keypair = keypair)

codeIndex = ts4.load_code_cell(VENDORING_PATH + 'compiled/Index.tvc')
codeData = ts4.load_code_cell(VENDORING_PATH + 'compiled/Data.tvc')

# 73616d706c652e75726c (in hex) = sample.url
iconUrl = "73616d706c652e75726c"
nftRoot = ts4.BaseContract('compiled/NftRoot', ctor_params = {'codeIndex': codeIndex, 'codeData': codeData, 'ownerPubkey': keypair[1], 'iconUrl': iconUrl}, keypair = keypair)

ts4.dispatch_messages()

#id
IRequiredInterfaces = 1
IStoreIPFS = 3
ReqInterfaces = [IRequiredInterfaces, IStoreIPFS]

answReqInterfaces = nftRoot.call_getter('getRequiredInterfaces')
answIconUrl = nftRoot.call_getter('getIconUrl')

assert eq(answIconUrl, iconUrl)
assert eq(answReqInterfaces, ReqInterfaces)