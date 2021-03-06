// 12/10

var searchBST = function(root, val) {
  if (root === null) return null;
  if (root.val === val) return root;

  if (val < root.val) {
    return searchBST(root.left, val);
  } else {
    return searchBST(root.right, val);
  }
};
