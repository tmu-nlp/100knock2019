'''
68. ソート
"dance"というタグを付与されたアーティストの中でレーティングの投票数が多いアーティスト・トップ10を求めよ．
'''


'''
> db.artist_collection.find({'tags.value':'dance'}, {'name': true}).limit(10)
{ "_id" : ObjectId("5cfca16c6e18fb743880b7f2"), "name" : "SSHäuptling" }
{ "_id" : ObjectId("5cfca1776e18fb7438810dcf"), "name" : "Boy George" }
{ "_id" : ObjectId("5cfca1956e18fb74388234fc"), "name" : "Toni Basil" }
{ "_id" : ObjectId("5cfca1a76e18fb743882d3f1"), "name" : "Milk Inc." }
{ "_id" : ObjectId("5cfca1d06e18fb7438844c4f"), "name" : "digitalTRAFFIC" }
{ "_id" : ObjectId("5cfca1db6e18fb743884a42b"), "name" : "Bag Raiders" }
{ "_id" : ObjectId("5cfca1ea6e18fb7438853378"), "name" : "Syncopaths" }
{ "_id" : ObjectId("5cfca1fc6e18fb743885d07e"), "name" : "Kristina Supergenius" }
{ "_id" : ObjectId("5cfca1fc6e18fb743885d44a"), "name" : "MaRina" }
{ "_id" : ObjectId("5cfca1fd6e18fb743885dde5"), "name" : "Sliptide" }
'''
