library("igraph")
library("rjson")
library("stringi")
library("rlist")
library("RJSONIO")

db <- rjson::fromJSON(file = "data1.txt")

edges <- c()
names = c()
for (i in db) {
  name = i$name
  names <- append(names, name)
}
for (i in db) {
  related <- i$playlistAuthors
  for (r in related) {
    if (r %in% names) {
      if (i$name != r) {
        name = i$name
        edges <- append(edges, name)
        edges <- append(edges, r)
      }
    }
  }
}

g <- graph(edges=edges)

# COMMUNITY DETECTION

wc <- cluster_walktrap(g)
le <- cluster_leading_eigen(g)
eb <- cluster_edge_betweenness(g)

modularity(wc)

#V(g)$label <- sub("&", "&#038;", stri_trans_general(names(membership(wc)[V(g)]), "russian-latin/bgn"))

for (i in (1:14957)) {
  #V(g)[i]$label <- names(membership(wc)[V(g)[i]])
  value <- as.character(membership(wc)[[V(g)[i]]])
  V(g)[i]$wc <- value
  #g <- set_vertex_attr(g, 'wc', index = V(g)[i], value)
}

eb <- cluster_edge_betweenness(g)
le <- cluster_leading_eigen(g)

##fg <- cluster_fast_greedy(g)

# COUNT SHORTEST PATHS
distMatrix <- shortest.paths(g, v=V(g), to=V(g))
##lst <- lapply(as.data.frame(t(distMatrix)), c)
average_paths <- rowMeans(distMatrix*is.finite(distMatrix),na.rm=TRUE)

# COUNT PATHS TO AUTHOR
blockers_paths <- distMatrix[, 'ÓÑÏÅØÍÀß ÃÐÓÏÏÀ']
klinsky_paths <- distMatrix[, 'Êëèíñêîå']
lizzka_paths <- distMatrix[, 'ëèççêà']
ro_paths <- distMatrix[, 'Maryana Ro']
versus_paths <- distMatrix[, 'versusbattleru']
hypecamp_paths <- distMatrix[, 'HYPE CAMP']

#PAGE RANK
pagerank <- page.rank(g)

# ADD NEW DATA TO DB
new_db <- list()
for (i in db) {
  i$wc <- tryCatch({as.character(membership(wc)[[i$name]])}, error=function(error_condition) {"0"})
  i$eb <- tryCatch({as.character(membership(eb)[[i$name]])}, error=function(error_condition) {"0"})
  i$le <- tryCatch({as.character(membership(le)[[i$name]])}, error=function(error_condition) {"0"})
  i$shortest <- tryCatch({average_paths[[i$name]]}, error=function(error_condition) {"0"})
  i$pagerank <- tryCatch({pagerank$vector[i$name]}, error=function(error_condition) {"0"})
  i$blockers <- tryCatch({blockers_paths[[i$name]]}, error=function(error_condition) {"0"})
  i$versus <- tryCatch({versus_paths[[i$name]]}, error=function(error_condition) {"0"})
  i$veet1 <- tryCatch({ro_paths[[i$name]]}, error=function(error_condition) {"0"})
  i$veet2 <- tryCatch({ro_paths[[i$name]]}, error=function(error_condition) {"0"})
  i$rostar <- tryCatch({ro_paths[[i$name]]}, error=function(error_condition) {"0"})
  i$klinsky <- tryCatch({klinsky_paths[[i$name]]}, error=function(error_condition) {"0"})
  i$lizzka <- tryCatch({lizzka_paths[[i$name]]}, error=function(error_condition) {"0"})
  i$hypecamp <- tryCatch({hypecamp_paths[[i$name]]}, error=function(error_condition) {"0"})
  new_db[[i$id]] <- i
}

# SAVE IN JSON
exportJson <- toJSON(new_db)
write(exportJson, "new2.json")


# TRYING TO SAVE IN GEFX (DOESN'T WORK)
saveAsGEXF = function(g, filepath="converted_graph.gexf")
{
  require(igraph)
  require(rgexf)
  require(XML)
  
  # gexf nodes require two column data frame (id, label)
  # check if the input vertices has label already present
  # if not, just have the ids themselves as the label
  if(is.null(V(g)$label)) {
    V(g)$label <- as.character(V(g))
  }
  
  V(g)$label <- sub("&", "&amp;", V(g)$label)
  V(g)$label <- sub("¸", "e", V(g)$label)
  # similarily if edges does not have weight, add default 1 weight
  if(is.null(E(g)$weight)) {
    E(g)$weight <- rep.int(1, ecount(g))
  }
  
  nodes <- data.frame(cbind(V(g), V(g)$label))
  edges <- t(Vectorize(get.edge, vectorize.args='id')(g, 1:ecount(g)))
  
  # combine all node attributes into a matrix (and take care of & for xml)
  vAttrNames <- setdiff(list.vertex.attributes(g), "label") 
  nodesAtt <- data.frame(lapply(vAttrNames,
                                
                                function(attr) { 
                                  
                                  v = get.vertex.attribute(g, attr);
                                  
                                  if(typeof(v) == "character")
                                    
                                    v = sub("&", "&amp;", get.vertex.attribute(g, attr))
                                  
                                  v
                                  
                                }),
                         
                         stringsAsFactors = FALSE)
  
  colnames(nodesAtt) <- vAttrNames
  
  # combine all edge attributes into a matrix (and take care of & for xml)
  eAttrNames <- setdiff(list.edge.attributes(g), "weight") 
  edgesAtt <- data.frame(sapply(eAttrNames, function(attr) sub("&", "&amp;",get.edge.attribute(g, attr))))
  
  # combine all graph attributes into a meta-data
  graphAtt <- sapply(list.graph.attributes(g), function(attr) sub("&", "&amp;",get.graph.attribute(g, attr)))
  
  # generate the gexf object
  output <- write.gexf(nodes, edges, nodesAtt = nodesAtt$wc)
  
  print(output, "output2.gexf", replace=T)
}

saveAsGEXF(g, "output1.gexf") 
