# Backchan

Backchan is 4chan and Reddit hybrid.

It's short for backchannel (a secret line of communication).

It's an anonynomous imageboard with multimedia and news aggregator
functionality.

An upgrade on both Reddit and 4chan.

## Channels

A Channel is similar to a subreddit or a board.

A User with an account can create any board they want.

There are default channels that are already provided by the creator.

Each channel consists of initial posts.

Those posts then point to an undirected graph of posts.

## Posting

Posts are modeled as follows:
- Int: ID
- String: Author
- Array of Ints: Replies
- Array of Ints: References
- Date: PostDate
- String: Text
- String: FilePathImage
- String: FilePathPdf
- String: FilePath3DModel
- Graph: GraphData
- String: ExecutableCode

Any visitor can post on any given channel on Backchan.

The posts can be anonymous whether they have an account or not.

Posts will not be hierarchical like Reddit nor trees like 4chan.

They will be undirected graphs.

Posts can make references to posts made before and after post
creation.

Posts can be edited but versions will stored and displayed for access.

The posts can be: 
- simple text, 
- an image, 
- a video, 
- a pdf document that is scanned by the server, 
- a 3D model with optional animation data, 
- a graph of arbitrarily-labeled nodes, or 
- executable common lisp/scheme/clojure code that is sandboxed by the
  website.

The posts are formatted according to the org-mode specification.

However, LaTeX code blocks are rendered in full LaTeX symbols.

Code written on a post can use data from other posts and operate it on
its data, input, or output.
