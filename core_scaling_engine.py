"""
Core Ultra-Fast Scaling Engine - Fixed for Vercel Deployment
This is the main scaling engine that will be imported by API endpoints
"""

import os
import json
import asyncio
import logging
from datetime import datetime, timedelta
from typing import Dict, List, Optional, Tuple

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class UltraFastScalingEngine:
    """
    Ultra-Fast Scaling Engine optimized for serverless deployment
    Handles automatic scaling of successful revenue streams
    """
    
    def __init__(self):
        self.config = self._load_config()
        self.scaling_thresholds = {
            'revenue_threshold': float(os.getenv('SCALING_REVENUE_THRESHOLD', '500')),
            'growth_rate_threshold': float(os.getenv('SCALING_GROWTH_THRESHOLD', '20')),
            'conversion_threshold': float(os.getenv('SCALING_CONVERSION_THRESHOLD', '2')),
            'max_concurrent_scales': int(os.getenv('MAX_CONCURRENT_SCALES', '5'))
        }
        
        # Scaling multipliers for different actions
        self.scaling_multipliers = {
            'ad_spend': 1.5,
            'audience_expansion': 2.0,
            'price_optimization': 1.3,
            'content_variation': 1.8,
            'platform_expansion': 2.5
        }
        
        # Performance tracking
        self.performance_metrics = {
            'scales_executed': 0,
            'success_rate': 95.0,
            'total_revenue_increase': 0,
            'last_optimization': datetime.now().isoformat()
        }
    
    def _load_config(self) -> Dict:
        """Load configuration from environment variables"""
        return {
            'openai_api_key': os.getenv('OPENAI_API_KEY'),
            'daily_target': float(os.getenv('DAILY_TARGET', '1000')),
            'auto_scaling_enabled': os.getenv('AUTO_SCALING_ENABLED', 'true').lower() == 'true',
            'max_ad_spend': float(os.getenv('MAX_AD_SPEND', '1000')),
            'risk_tolerance': float(os.getenv('RISK_TOLERANCE', '0.7'))
        }
    
    async def analyze_scaling_opportunities(self, products: List[Dict]) -> List[Dict]:
        """
        Analyze products for scaling opportunities using AI
        Optimized for fast execution in serverless environment
        """
        try:
            scaling_candidates = []
            
            for product in products:
                # Fast metrics calculation
                metrics = await self._calculate_product_metrics(product)
                
                # Rapid opportunity scoring
                opportunity_score = self._calculate_opportunity_score(metrics)
                
                if opportunity_score >= 0.8:  # High confidence threshold
                    scaling_strategy = await self._generate_scaling_strategy(product, metrics)
                    scaling_candidates.append({
                        'product': product,
                        'metrics': metrics,
                        'opportunity_score': opportunity_score,
                        'scaling_strategy': scaling_strategy,
                        'estimated_roi': self._estimate_roi(metrics, scaling_strategy)
                    })
            
            # Sort by opportunity score and ROI
            scaling_candidates.sort(key=lambda x: x['opportunity_score'] * x['estimated_roi'], reverse=True)
            
            return scaling_candidates[:self.scaling_thresholds['max_concurrent_scales']]
            
        except Exception as e:
            logger.error(f"Error analyzing scaling opportunities: {str(e)}")
            return []
    
    async def _calculate_product_metrics(self, product: Dict) -> Dict:
        """Calculate key metrics for scaling decision"""
        try:
            # Get current metrics
            current_revenue = product.get('daily_revenue', 0)
            historical_data = product.get('historical_data', [])
            
            if len(historical_data) < 2:
                # Default metrics for new products
                return {
                    'current_revenue': current_revenue,
                    'growth_rate': 25.0,  # Default growth rate
                    'conversion_rate': product.get('conversion_rate', 2.5),
                    'traffic_volume': product.get('traffic_volume', 1000),
                    'profit_margin': product.get('profit_margin', 0.7),
                    'customer_acquisition_cost': product.get('cac', 50),
                    'lifetime_value': product.get('ltv', 200)
                }
            
            # Calculate growth rate from historical data
            recent_avg = sum(historical_data[-7:]) / min(7, len(historical_data))
            older_avg = sum(historical_data[-14:-7]) / min(7, len(historical_data[-14:-7]))
            growth_rate = ((recent_avg - older_avg) / older_avg * 100) if older_avg > 0 else 25.0
            
            return {
                'current_revenue': current_revenue,
                'growth_rate': growth_rate,
                'conversion_rate': product.get('conversion_rate', 2.5),
                'traffic_volume': product.get('traffic_volume', 1000),
                'profit_margin': product.get('profit_margin', 0.7),
                'customer_acquisition_cost': product.get('cac', 50),
                'lifetime_value': product.get('ltv', 200)
            }
            
        except Exception as e:
            logger.error(f"Error calculating metrics: {str(e)}")
            return {
                'current_revenue': 0,
                'growth_rate': 0,
                'conversion_rate': 0,
                'traffic_volume': 0,
                'profit_margin': 0.7,
                'customer_acquisition_cost': 50,
                'lifetime_value': 200
            }
    
    def _calculate_opportunity_score(self, metrics: Dict) -> float:
        """Calculate opportunity score using weighted factors"""
        try:
            # Weighted scoring factors
            weights = {
                'revenue_factor': 0.3,
                'growth_factor': 0.25,
                'conversion_factor': 0.2,
                'profit_factor': 0.15,
                'efficiency_factor': 0.1
            }
            
            # Calculate individual scores (0-1 scale)
            revenue_score = min(metrics.get('current_revenue', 0) / self.scaling_thresholds['revenue_threshold'], 1.0)
            growth_score = min(metrics.get('growth_rate', 0) / 100, 1.0)
            conversion_score = min(metrics.get('conversion_rate', 0) / 10, 1.0)
            profit_score = min(metrics.get('profit_margin', 0), 1.0)
            
            # Efficiency score (LTV/CAC ratio)
            ltv = metrics.get('lifetime_value', 0)
            cac = metrics.get('customer_acquisition_cost', 1)
            efficiency_score = min(ltv / cac / 5, 1.0) if cac > 0 else 0
            
            # Calculate weighted total
            total_score = (
                revenue_score * weights['revenue_factor'] +
                growth_score * weights['growth_factor'] +
                conversion_score * weights['conversion_factor'] +
                profit_score * weights['profit_factor'] +
                efficiency_score * weights['efficiency_factor']
            )
            
            return max(0.0, min(1.0, total_score))
            
        except Exception as e:
            logger.error(f"Error calculating opportunity score: {str(e)}")
            return 0.0
    
    async def _generate_scaling_strategy(self, product: Dict, metrics: Dict) -> Dict:
        """Generate AI-powered scaling strategy"""
        try:
            # Determine best scaling actions based on metrics
            strategy = {
                'actions': [],
                'budget_allocation': {},
                'timeline': 'immediate',
                'expected_roi': 0,
                'risk_level': 'medium'
            }
            
            current_revenue = metrics.get('current_revenue', 0)
            growth_rate = metrics.get('growth_rate', 0)
            conversion_rate = metrics.get('conversion_rate', 0)
            
            # High-impact scaling actions
            if current_revenue >= self.scaling_thresholds['revenue_threshold']:
                strategy['actions'].append({
                    'type': 'ad_spend_increase',
                    'multiplier': self.scaling_multipliers['ad_spend'],
                    'budget': min(current_revenue * 0.3, self.config['max_ad_spend']),
                    'expected_increase': current_revenue * 0.5
                })
            
            if growth_rate > self.scaling_thresholds['growth_rate_threshold']:
                strategy['actions'].append({
                    'type': 'audience_expansion',
                    'multiplier': self.scaling_multipliers['audience_expansion'],
                    'budget': current_revenue * 0.2,
                    'expected_increase': current_revenue * 0.8
                })
            
            if conversion_rate > self.scaling_thresholds['conversion_threshold']:
                strategy['actions'].append({
                    'type': 'platform_expansion',
                    'multiplier': self.scaling_multipliers['platform_expansion'],
                    'budget': current_revenue * 0.4,
                    'expected_increase': current_revenue * 1.2
                })
            
            # Always add price optimization for existing products
            strategy['actions'].append({
                'type': 'price_optimization',
                'multiplier': self.scaling_multipliers['price_optimization'],
                'budget': current_revenue * 0.1,
                'expected_increase': current_revenue * 0.3
            })
            
            # Calculate expected ROI
            total_investment = sum(action['budget'] for action in strategy['actions'])
            total_expected_return = sum(action['expected_increase'] for action in strategy['actions'])
            
            if total_investment > 0:
                strategy['expected_roi'] = (total_expected_return / total_investment - 1) * 100
            else:
                strategy['expected_roi'] = 0
            
            return strategy
            
        except Exception as e:
            logger.error(f"Error generating scaling strategy: {str(e)}")
            return {
                'actions': [],
                'expected_roi': 0,
                'timeline': 'immediate',
                'risk_level': 'low'
            }
    
    def _estimate_roi(self, metrics: Dict, strategy: Dict) -> float:
        """Estimate ROI for scaling strategy"""
        try:
            base_roi = strategy.get('expected_roi', 0)
            
            # Adjust based on historical performance
            growth_rate = metrics.get('growth_rate', 0)
            conversion_rate = metrics.get('conversion_rate', 0)
            
            # Boost ROI estimate for high-performing products
            if growth_rate > 50:
                base_roi *= 1.3
            if conversion_rate > 5:
                base_roi *= 1.2
            
            # Apply risk factors
            risk_adjustment = 1.0
            if strategy.get('risk_level') == 'high':
                risk_adjustment = 0.8
            elif strategy.get('risk_level') == 'low':
                risk_adjustment = 1.1
            
            return max(0.0, min(500.0, base_roi * risk_adjustment))
            
        except Exception as e:
            logger.error(f"Error estimating ROI: {str(e)}")
            return 0.0
    
    async def execute_scaling_actions(self, scaling_candidates: List[Dict]) -> Dict:
        """Execute scaling actions asynchronously"""
        try:
            start_time = datetime.now()
            
            results = {
                'executed_actions': 0,
                'total_investment': 0,
                'expected_return': 0,
                'failed_actions': 0,
                'success_rate': 0,
                'execution_time': 0
            }
            
            # Execute actions concurrently
            tasks = []
            for candidate in scaling_candidates:
                for action in candidate['scaling_strategy']['actions']:
                    task = asyncio.create_task(
                        self._execute_single_action(candidate['product'], action)
                    )
                    tasks.append(task)
            
            # Wait for all actions to complete (with timeout)
            try:
                action_results = await asyncio.wait_for(
                    asyncio.gather(*tasks, return_exceptions=True),
                    timeout=30.0  # 30 second timeout
                )
            except asyncio.TimeoutError:
                logger.warning("Scaling execution timed out")
                action_results = [{'investment': 0, 'expected_return': 0, 'status': 'timeout'}] * len(tasks)
            
            # Process results
            for result in action_results:
                if isinstance(result, Exception):
                    results['failed_actions'] += 1
                    logger.error(f"Action failed: {str(result)}")
                else:
                    results['executed_actions'] += 1
                    results['total_investment'] += result.get('investment', 0)
                    results['expected_return'] += result.get('expected_return', 0)
            
            # Calculate success rate
            total_actions = len(action_results)
            if total_actions > 0:
                results['success_rate'] = (results['executed_actions'] / total_actions) * 100
            
            # Calculate execution time
            execution_time = (datetime.now() - start_time).total_seconds()
            results['execution_time'] = execution_time
            
            # Update performance metrics
            self.performance_metrics['scales_executed'] += results['executed_actions']
            self.performance_metrics['success_rate'] = results['success_rate']
            self.performance_metrics['total_revenue_increase'] += results['expected_return']
            self.performance_metrics['last_optimization'] = datetime.now().isoformat()
            
            return results
            
        except Exception as e:
            logger.error(f"Error executing scaling actions: {str(e)}")
            return {
                'executed_actions': 0,
                'total_investment': 0,
                'expected_return': 0,
                'failed_actions': 1,
                'success_rate': 0,
                'execution_time': 0
            }
    
    async def _execute_single_action(self, product: Dict, action: Dict) -> Dict:
        """Execute a single scaling action"""
        try:
            action_type = action['type']
            
            # Route to appropriate action handler
            if action_type == 'ad_spend_increase':
                return await self._increase_ad_spend(product, action)
            elif action_type == 'audience_expansion':
                return await self._expand_audience(product, action)
            elif action_type == 'platform_expansion':
                return await self._expand_platforms(product, action)
            elif action_type == 'price_optimization':
                return await self._optimize_pricing(product, action)
            else:
                logger.warning(f"Unknown action type: {action_type}")
                return {
                    'investment': 0,
                    'expected_return': 0,
                    'action_type': action_type,
                    'status': 'unknown_action'
                }
                
        except Exception as e:
            logger.error(f"Error executing action {action.get('type', 'unknown')}: {str(e)}")
            raise
    
    async def _increase_ad_spend(self, product: Dict, action: Dict) -> Dict:
        """Increase advertising spend for product"""
        try:
            budget = action['budget']
            expected_increase = action['expected_increase']
            
            # Simulate ad spend increase (replace with actual API calls)
            await asyncio.sleep(0.1)  # Simulate API call delay
            
            logger.info(f"Increased ad spend by ${budget:.2f} for product {product.get('name', 'unknown')}")
            
            return {
                'investment': budget,
                'expected_return': expected_increase,
                'action_type': 'ad_spend_increase',
                'status': 'success'
            }
            
        except Exception as e:
            logger.error(f"Error increasing ad spend: {str(e)}")
            return {
                'investment': 0,
                'expected_return': 0,
                'action_type': 'ad_spend_increase',
                'status': 'failed'
            }
    
    async def _expand_audience(self, product: Dict, action: Dict) -> Dict:
        """Expand target audience for product"""
        try:
            budget = action['budget']
            expected_increase = action['expected_increase']
            
            # Simulate audience expansion (replace with actual API calls)
            await asyncio.sleep(0.1)
            
            logger.info(f"Expanded audience targeting for product {product.get('name', 'unknown')}")
            
            return {
                'investment': budget,
                'expected_return': expected_increase,
                'action_type': 'audience_expansion',
                'status': 'success'
            }
            
        except Exception as e:
            logger.error(f"Error expanding audience: {str(e)}")
            return {
                'investment': 0,
                'expected_return': 0,
                'action_type': 'audience_expansion',
                'status': 'failed'
            }
    
    async def _expand_platforms(self, product: Dict, action: Dict) -> Dict:
        """Expand product to new platforms"""
        try:
            budget = action['budget']
            expected_increase = action['expected_increase']
            
            # Simulate platform expansion
            await asyncio.sleep(0.1)
            
            logger.info(f"Expanded to new platforms for product {product.get('name', 'unknown')}")
            
            return {
                'investment': budget,
                'expected_return': expected_increase,
                'action_type': 'platform_expansion',
                'status': 'success'
            }
            
        except Exception as e:
            logger.error(f"Error expanding platforms: {str(e)}")
            return {
                'investment': 0,
                'expected_return': 0,
                'action_type': 'platform_expansion',
                'status': 'failed'
            }
    
    async def _optimize_pricing(self, product: Dict, action: Dict) -> Dict:
        """Optimize product pricing"""
        try:
            budget = action.get('budget', 0)
            expected_increase = action['expected_increase']
            
            # Simulate pricing optimization
            await asyncio.sleep(0.1)
            
            logger.info(f"Optimized pricing for product {product.get('name', 'unknown')}")
            
            return {
                'investment': budget,
                'expected_return': expected_increase,
                'action_type': 'price_optimization',
                'status': 'success'
            }
            
        except Exception as e:
            logger.error(f"Error optimizing pricing: {str(e)}")
            return {
                'investment': 0,
                'expected_return': 0,
                'action_type': 'price_optimization',
                'status': 'failed'
            }
    
    def get_performance_metrics(self) -> Dict:
        """Get current performance metrics"""
        return self.performance_metrics.copy()
    
    async def run_scaling_cycle(self, products: List[Dict]) -> Dict:
        """Run complete scaling cycle"""
        try:
            start_time = datetime.now()
            
            # Step 1: Analyze opportunities
            scaling_candidates = await self.analyze_scaling_opportunities(products)
            
            if not scaling_candidates:
                return {
                    'status': 'no_opportunities',
                    'message': 'No scaling opportunities found meeting criteria',
                    'scaling_candidates': 0,
                    'execution_time': (datetime.now() - start_time).total_seconds()
                }
            
            # Step 2: Execute scaling actions
            results = await self.execute_scaling_actions(scaling_candidates)
            
            # Step 3: Return comprehensive results
            return {
                'status': 'success',
                'message': f'Scaling cycle completed with {results["executed_actions"]} actions',
                'scaling_candidates': len(scaling_candidates),
                'execution_results': results,
                'performance_metrics': self.get_performance_metrics(),
                'execution_time': (datetime.now() - start_time).total_seconds()
            }
            
        except Exception as e:
            logger.error(f"Error in scaling cycle: {str(e)}")
            return {
                'status': 'error',
                'message': f'Scaling cycle failed: {str(e)}',
                'scaling_candidates': 0,
                'execution_time': (datetime.now() - start_time).total_seconds()
            }

# Factory function for serverless environments
def create_scaling_engine():
    """Create scaling engine instance"""
    return UltraFastScalingEngine()

# Singleton instance for API endpoints
_scaling_engine_instance = None

def get_scaling_engine():
    """Get singleton scaling engine instance"""
    global _scaling_engine_instance
    if _scaling_engine_instance is None:
        _scaling_engine_instance = create_scaling_engine()
    return _scaling_engine_instance

# Example usage for testing
async def test_scaling_engine():
    """Test the scaling engine"""
    engine = create_scaling_engine()
    
    # Sample product data
    sample_products = [
        {
            'name': 'AI Writing Tool',
            'daily_revenue': 750,
            'conversion_rate': 3.2,
            'traffic_volume': 1000,
            'historical_data': [500, 550, 600, 650, 700, 750, 800, 850, 900, 950, 1000],
            'profit_margin': 0.8
        },
        {
            'name': 'Digital Course',
            'daily_revenue': 1200,
            'conversion_rate': 2.8,
            'traffic_volume': 1500,
            'historical_data': [800, 850, 900, 950, 1000, 1050, 1100, 1150, 1200, 1250, 1300],
            'profit_margin': 0.9
        }
    ]
    
    # Run scaling cycle
    result = await engine.run_scaling_cycle(sample_products)
    return result

if __name__ == "__main__":
    # For local testing
    async def main():
        result = await test_scaling_engine()
        print(json.dumps(result, indent=2))
    
    asyncio.run(main())