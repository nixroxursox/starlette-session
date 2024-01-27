/* global use, db */
// MongoDB Playground
// Use Ctrl+Space inside a snippet or a string literal to trigger completions.

// The current database to use.
use('NCKeno');

// Search for documents in the current collection.
db.getCollection('keno_data')
  .find(
    {
      'draw number': '*'
      /*
      * Filter
      * fieldA: value or expression
      */
    },
  )
  .sort({
    /*
    * fieldA: 1 // ascending
    * fieldB: -1 // descending
    */
  });
