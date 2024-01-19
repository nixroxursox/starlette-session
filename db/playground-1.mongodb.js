/* global use, db */
// MongoDB Playground
// Use Ctrl+Space inside a snippet or a string literal to trigger completions.

// The current database to use.
use('eCom');

// Search for documents in the current collection.
db.getCollection('session_data')
  .findOne(
    {
      'reg_data.userId': '*'
      /*
      * Filter
      * fieldA: value or expression
      */
    },
    {
      /*
      * Projection
      * _id: 0, // exclude _id
      * fieldA: 1 // include field
      */
     'session_data.session_id': 1,
     'session_data.metadata.lifetime': 1
    }
  )
  .sort({
    /*
    * fieldA: 1 // ascending
    * fieldB: -1 // descending
    */
  });
