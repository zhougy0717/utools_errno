const linuxErrno = require('./linux_errno.json')
const gpTeeReturnCode = require('./gp_tee.json')
const osslTlsErrno = require('./openssl_tls_errno.json')

let g_items = []
window.exports = {
  'errno': {
    mode: 'list',
    args: {
      enter: (action, callbackSetList) => {
        let linuxErrno = require('./linux_errno.json')
        linuxErrno.forEach(x => {
          x.keywords = x.title + x.description + 'linux'
        })
        let gpTeeReturnCode = require('./gp_tee.json')
        gpTeeReturnCode.forEach(x => {
          x.keywords = x.title + x.description + 'tee'
        })
        let osslTlsErrno = require('./openssl_tls_errno.json')
        osslTlsErrno.forEach(x => {
          x.keywords = x.title + x.description + 'openssl ossl tls'
        })
        let httpErrno = require('./http_errno.json')
        httpErrno.forEach(x => {
          x.keywords = x.title + x.description + 'http'
        })
        g_items = g_items.concat(linuxErrno).concat(gpTeeReturnCode).concat(osslTlsErrno).concat(httpErrno)
        g_items.forEach(x => {
          x.keywords = x.keywords.toLowerCase()
        })
      },
      search: (action, searchWord, callbackSetList) => {
        const filtered = g_items.filter(x => {
          const words = searchWord.toLowerCase().split(' ')
          for (let i = 0; i < words.length; i++) {
            let hit = true
            hit = hit && x.keywords.includes(words[i])
            if (!hit) {
              return false
            }
          }
          return true
        })
        return callbackSetList(filtered)
      },
      select: (action, itemData) => {},
      placeholder: "搜索错误码"
    }
  }
}
