#ifndef ICHiggsTauTau_CombineTools_Systematics_h
#define ICHiggsTauTau_CombineTools_Systematics_h
#include<string>
#include "CombineTools/interface/Process.h"

namespace ch {
namespace syst {

  struct bin {
    typedef std::string type;
    inline static type get(ch::Process *p) { return p->bin(); }
  };

  struct analysis {
    typedef std::string type;
    inline static type get(ch::Process *p) { return p->analysis(); }
  };

  struct era {
    typedef std::string type;
    inline static type get(ch::Process *p) { return p->era(); }
  };

  struct channel {
    typedef std::string type;
    inline static type get(ch::Process *p) { return p->channel(); }
  };

  struct mass {
    typedef std::string type;
    inline static type get(ch::Process *p) { return p->mass(); }
  };

  struct process {
    typedef std::string type;
    inline static type get(ch::Process *p) { return p->process(); }
  };

  class bin_id {
   public:
    typedef int type;
    inline static type get(ch::Process *p) { return p->bin_id(); }
  };

  namespace detail {
    template <typename F>
    inline void cross_imp(F f) {
      f();
    }
    template <typename F, typename H, typename... Ts>
    inline void cross_imp(F f, std::vector<H> const &h,
                          std::vector<Ts> const &... t) {
      for (H const &he : h)
        cross_imp([&](Ts const &... ts) { f(he, ts...); }, t...);
    }

    template <typename... Ts>
    std::vector<std::tuple<Ts...>> cross(std::vector<Ts> const &... in) {
      std::vector<std::tuple<Ts...>> res;
      cross_imp([&](Ts const &... ts) {
        res.emplace_back(ts...);
      }, in...);
      return res;
    }
  }

  template<class... T>
  class SystMap {
   private:
    std::map<std::tuple<typename T::type...>, double> tmap_;

   public:
    SystMap& operator()(std::vector<typename T::type>... input, double val) {
      auto res = ch::syst::detail::cross(input...);
      for (auto const& a : res) tmap_.insert(std::make_pair(a, val));
      return *this;
    }

    bool Contains(ch::Process *p) const {
      if (p) {
        return tmap_.count(std::make_tuple(T::get(p)...));
      } else {
        return false;
      }
    }

    double Val(ch::Process *p) const {
      if (p) {
        return tmap_.find(std::make_tuple(T::get(p)...))->second;
      } else {
        return 0.0;
      }
    }

    static SystMap<T...> init(std::vector<typename T::type>... input, double val) {
      SystMap<T...> x;
      return x(input..., val);
    }
  };

  // template<class... T>
  // auto syst_map(std::vector<typename T::type>... input, double val) -> SystMap<T...> {
  //   SystMap<T...> x;
  //   return x(input..., val);
  // }

}
}

#endif
