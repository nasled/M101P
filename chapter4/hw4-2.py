#!/usr/bin/env python
import pymongo

def _finditem(obj, key):
    if key in obj:
        return obj[key]

    for k, v in obj.items():
        if isinstance(v,dict):
            item = _finditem(v, key)

            if item is not None:
                return item


explain = {
    "queryPlanner" : {
        "plannerVersion" : 1,
        "namespace" : "twitter.tweets",
        "indexFilterSet" : False,
        "parsedQuery" : {
            "user.followers_count" : {
                "$gt" : 1000
            }
        },
        "winningPlan" : {
            "stage" : "LIMIT",
            "limitAmount" : 0,
            "inputStage" : {
                "stage" : "SKIP",
                "skipAmount" : 0,
                "inputStage" : {
                    "stage" : "FETCH",
                    "filter" : {
                        "user.followers_count" : {
                            "$gt" : 1000
                        }
                    },
                    "inputStage" : {
                        "stage" : "IXSCAN",
                        "keyPattern" : {
                            "created_at" : -1
                        },
                        "indexName" : "created_at_-1",
                        "isMultiKey" : True,
                        "direction" : "backward",
                        "indexBounds" : {
                            "created_at" : [
                                "[MinKey, MaxKey]"
                            ]
                        }
                    }
                }
            }
        },
        "rejectedPlans" : [ ]
    },
    "executionStats" : {
        "executionSuccess" : True,
        "nReturned" : 10,
        "executionTimeMillis" : 563,
        "totalKeysExamined" : 251120,
        "totalDocsExamined" : 251120,
        "executionStages" : {
            "stage" : "LIMIT",
            "nReturned" : 10,
            "executionTimeMillisEstimate" : 500,
            "works" : 251121,
            "advanced" : 10,
            "needTime" : 251110,
            "needFetch" : 0,
            "saveState" : 1961,
            "restoreState" : 1961,
            "isEOF" : 1,
            "invalidates" : 0,
            "limitAmount" : 0,
            "inputStage" : {
                "stage" : "SKIP",
                "nReturned" : 10,
                "executionTimeMillisEstimate" : 500,
                "works" : 251120,
                "advanced" : 10,
                "needTime" : 251110,
                "needFetch" : 0,
                "saveState" : 1961,
                "restoreState" : 1961,
                "isEOF" : 0,
                "invalidates" : 0,
                "skipAmount" : 0,
                "inputStage" : {
                    "stage" : "FETCH",
                    "filter" : {
                        "user.followers_count" : {
                            "$gt" : 1000
                        }
                    },
                    "nReturned" : 5010,
                    "executionTimeMillisEstimate" : 490,
                    "works" : 251120,
                    "advanced" : 5010,
                    "needTime" : 246110,
                    "needFetch" : 0,
                    "saveState" : 1961,
                    "restoreState" : 1961,
                    "isEOF" : 0,
                    "invalidates" : 0,
                    "docsExamined" : 251120,
                    "alreadyHasObj" : 0,
                    "inputStage" : {
                        "stage" : "IXSCAN",
                        "nReturned" : 251120,
                        "executionTimeMillisEstimate" : 100,
                        "works" : 251120,
                        "advanced" : 251120,
                        "needTime" : 0,
                        "needFetch" : 0,
                        "saveState" : 1961,
                        "restoreState" : 1961,
                        "isEOF" : 0,
                        "invalidates" : 0,
                        "keyPattern" : {
                            "created_at" : -1
                        },
                        "indexName" : "created_at_-1",
                        "isMultiKey" : False,
                        "direction" : "backward",
                        "indexBounds" : {
                            "created_at" : [
                                "[MinKey, MaxKey]"
                            ]
                        },
                        "keysExamined" : 251120,
                        "dupsTested" : 0,
                        "dupsDropped" : 0,
                        "seenInvalidated" : 0,
                        "matchTested" : 0
                    }
                }
            }
        }
    },
    "serverInfo" : {
        "host" : "generic-name.local",
        "port" : 27017,
        "version" : "3.0.1",
        "gitVersion" : "534b5a3f9d10f00cd27737fbcd951032248b5952"
    },
    "ok" : 1
}

result1 = 'indexName' in explain['executionStats']['executionStages']['inputStage']['inputStage']['inputStage']
result2 = 'indexName' in explain['executionStats']['executionStages']['inputStage']['inputStage']
result3 = True if (explain['executionStats']['nReturned'] == 251120) else False
result4 = True if (explain['executionStats']['totalDocsExamined'] == 251120) else False
result5 = True if (explain['executionStats']['totalDocsExamined'] == 0) else False

# The query uses an index to determine the order in which to return result documents:  True
# The query uses an index to determine which documents match:  False
# The query returns 251120 documents:  False
# The query examines 251120 documents:  True
# The query is a covered query:  False

print('The query uses an index to determine the order in which to return result documents: ', result1)
print('The query uses an index to determine which documents match: ', result2)
print('The query returns 251120 documents: ', result3)
print('The query examines 251120 documents: ', result4)
print('The query is a covered query: ', result5)