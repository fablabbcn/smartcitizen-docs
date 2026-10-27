window.MathJax = {
  tex: {
    inlineMath: [["\\(", "\\)"]],
    displayMath: [["\\[", "\\]"]],
    processEscapes: true,
    processEnvironments: true
  },
  options: {
    ignoreHtmlClass: ".*|",
    processHtmlClass: "arithmatex"
  },
  // Typesetting is done below on every page load, including instant
  // navigation. Typesetting on startup too renders equations twice.
  startup: {
    typeset: false
  }
};

document$.subscribe(() => {
  if (!MathJax.startup) return
  MathJax.startup.promise.then(() => {
    MathJax.startup.output.clearCache()
    MathJax.typesetClear()
    MathJax.texReset()
    return MathJax.typesetPromise()
  })
})
